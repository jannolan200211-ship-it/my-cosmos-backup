#!/usr/bin/env python3
"""
distill.py - Main distillation script for memory librarian

This script orchestrates the complete distillation cycle:
1. RAM safety check
2. Workspace scanning
3. Importance scoring
4. INDEX.md update
5. Topic file management
6. Archiving
7. Logging and notification
"""

import os
import sys
import time
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Tuple

# Configuration
WORKSPACE_DIR = Path("/root/.openclaw/workspace")
MEMORY_DIR = Path("/root/.openclaw/memory")
TOPICS_DIR = MEMORY_DIR / "topics"
ARCHIVE_DIR = MEMORY_DIR / "archive"
LOG_FILE = Path("/root/.openclaw/logs/librarian.log")
INDEX_FILE = MEMORY_DIR / "INDEX.md"

# RAM threshold (in percentage)
RAM_THRESHOLD = 90

# Importance scoring weights
SCORE_TAG_IMPORTANT = 100
SCORE_TAG_URGENT = 90
SCORE_TAG_TODO = 70
SCORE_RECENCY_1D = 50
SCORE_RECENCY_7D = 30
SCORE_RECENCY_30D = 10

class LibrarianLogger:
    """Simple logger for librarian operations"""
    
    def __init__(self, log_file: Path):
        self.log_file = log_file
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {message}\n"
        print(log_line.strip())
        with open(self.log_file, 'a') as f:
            f.write(log_line)

def check_ram() -> Tuple[bool, int, str]:
    """
    Check RAM usage and determine if it's safe to proceed
    Returns: (is_safe, ram_percent, ram_status_message)
    """
    try:
        result = subprocess.run(
            ['free', '-m'],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split('\n')
        mem_line = lines[1].split()
        total = int(mem_line[1])
        used = int(mem_line[2])
        percent = int((used / total) * 100)
        
        is_safe = percent < RAM_THRESHOLD
        status = f"{used}MB / {total}MB ({percent}%)"
        
        return is_safe, percent, status
    except Exception as e:
        return False, 100, f"Error checking RAM: {e}"

def scan_workspace() -> List[Path]:
    """
    Scan workspace directory for all files using ripgrep for efficiency
    Returns list of file paths
    """
    files = []
    try:
        # Use ripgrep to get file list - much faster and more RAM efficient than os.walk
        result = subprocess.run(
            ['rg', '--files', str(WORKSPACE_DIR)],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.strip().split('\n'):
            if line:
                files.append(Path(line))
    except Exception as e:
        print(f"Error scanning workspace with ripgrep: {e}")
        # Fallback to os.walk if ripgrep fails
        try:
            for root, dirs, filenames in os.walk(WORKSPACE_DIR):
                dirs[:] = [d for d in dirs if not d.startswith('.') 
                           and d not in ['node_modules', 'dist', '__pycache__']]
                for filename in filenames:
                    if not filename.startswith('.'):
                        files.append(Path(root) / filename)
        except Exception as walk_e:
            print(f"Fallback scan also failed: {walk_e}")
    
    return files

def calculate_importance_score(file_path: Path) -> int:
    """
    Calculate importance score for a file based on:
    - User tags (#IMPORTANT, #URGENT, #TODO)
    - Recency (modification time)
    - Access frequency (if tracked)
    """
    score = 0
    
    try:
        # Check for user tags by reading file content
        # NOTE: In production, Claude should use ripgrep for efficiency
        # For now, we check file size first to avoid reading huge files
        if file_path.stat().st_size < 1024 * 1024:  # < 1MB
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                if '#IMPORTANT' in content:
                    score += SCORE_TAG_IMPORTANT
                if '#URGENT' in content:
                    score += SCORE_TAG_URGENT
                if '#TODO' in content:
                    score += SCORE_TAG_TODO
        
        # Recency score
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        age = datetime.now() - mtime
        
        if age < timedelta(days=1):
            score += SCORE_RECENCY_1D
        elif age < timedelta(days=7):
            score += SCORE_RECENCY_7D
        elif age < timedelta(days=30):
            score += SCORE_RECENCY_30D
        
        # TODO: Access frequency tracking could be added here
        # For now, we don't have that data
        
    except Exception as e:
        print(f"Error scoring {file_path}: {e}")
    
    return score

def update_index(active_projects: List[Dict], topic_map: Dict[str, str], 
                 stats: Dict):
    """
    Update INDEX.md with current state
    """
    try:
        content = f"""# 📌 GLOBAL_KNOWLEDGE_INDEX

Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🔥 ACTIVE_PROJECTS

"""
        # Add active projects
        for project in active_projects:
            content += f"""### Project: {project['name']}
- **Status**: {project.get('status', 'Unknown')}
- **Priority**: {project.get('priority', 'Medium')}
- **Files**: {', '.join(project.get('files', []))}
- **Last Modified**: {project.get('last_modified', 'Unknown')}
- **Summary**: {project.get('summary', 'No summary available')}

"""
        
        content += """## 📂 TOPIC_MAP

"""
        # Add topic map
        for topic, path in sorted(topic_map.items()):
            content += f"- **{topic}** → `{path}`\n"
        
        content += f"""
## ⏱️ LAST_DISTILLATION

- **Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Duration**: {stats.get('duration', 0)}s
- **Topics Updated**: {stats.get('topics_updated', 0)}
- **Files Archived**: {stats.get('files_archived', 0)}
- **RAM Usage**: {stats.get('ram_status', 'Unknown')}
"""
        
        INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(INDEX_FILE, 'w') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error updating INDEX.md: {e}")
        return False

def archive_old_files(days_threshold: int = 30) -> int:
    """
    Archive files older than threshold days with low importance score
    Returns number of files archived
    """
    archived_count = 0
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    
    try:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        
        for file_path in scan_workspace():
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            score = calculate_importance_score(file_path)
            
            # Archive if old and low priority
            if mtime < cutoff_date and score < 40:
                # Create same directory structure in archive
                rel_path = file_path.relative_to(WORKSPACE_DIR)
                archive_path = ARCHIVE_DIR / rel_path
                archive_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Move file
                file_path.rename(archive_path)
                archived_count += 1
    except Exception as e:
        print(f"Error archiving files: {e}")
    
    return archived_count

def send_notification(stats: Dict):
    """
    Send Telegram notification with distillation results
    """
    try:
        script_path = Path(__file__).parent / "notify.sh"
        subprocess.run([
            'bash',
            str(script_path),
            '',  # Message will be built in script
            str(stats.get('topics_updated', 0)),
            str(stats.get('files_archived', 0)),
            str(stats.get('active_projects', 0)),
            str(stats.get('ram_percent', 0)),
            str(stats.get('duration', 0))
        ])
    except Exception as e:
        print(f"Error sending notification: {e}")

def main():
    """
    Main distillation orchestration
    """
    start_time = time.time()
    logger = LibrarianLogger(LOG_FILE)
    
    logger.log("=" * 60)
    logger.log("Distillation cycle started")
    
    # Step 1: RAM safety check
    is_safe, ram_percent, ram_status = check_ram()
    logger.log(f"RAM check: {ram_status} - {'OK' if is_safe else 'LOW_MEMORY_MODE'}")
    
    if not is_safe:
        logger.log("⚠️ RAM usage high - using low-memory mode")
        # In low-memory mode, only update index, skip heavy operations
    
    # Step 2: Scan workspace
    logger.log("Scanning workspace...")
    files = scan_workspace()
    logger.log(f"Found {len(files)} files in workspace")
    
    # Step 3: Calculate importance scores and identify priorities
    logger.log("Calculating importance scores...")
    high_priority_files = []
    for file_path in files:
        score = calculate_importance_score(file_path)
        if score > 80:
            high_priority_files.append((file_path, score))
    
    logger.log(f"Found {len(high_priority_files)} high-priority files")
    
    # Step 4: Extract active projects
    # NOTE: This is where Claude (David) would step in to:
    # - Read high-priority files
    # - Extract project information
    # - Categorize and summarize
    active_projects = []
    
    # Placeholder: In production, Claude would do this intelligently
    for file_path, score in high_priority_files[:10]:  # Limit to top 10
        active_projects.append({
            'name': file_path.stem,
            'status': 'In Progress',
            'priority': '#IMPORTANT' if score > 100 else 'High',
            'files': [str(file_path.relative_to(WORKSPACE_DIR))],
            'last_modified': datetime.fromtimestamp(
                file_path.stat().st_mtime
            ).strftime('%Y-%m-%d'),
            'summary': f'Score: {score}'
        })
    
    # Step 5: Build topic map
    topic_map = {}
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    
    for topic_file in TOPICS_DIR.glob("*.md"):
        topic_name = topic_file.stem.replace('-', ' ').title()
        topic_map[topic_name] = str(topic_file.relative_to(MEMORY_DIR))
    
    logger.log(f"Current topic map has {len(topic_map)} topics")
    
    # Step 6: Archive old files
    if is_safe:  # Only archive in safe mode
        logger.log("Archiving old files...")
        archived_count = archive_old_files()
        logger.log(f"Archived {archived_count} files")
    else:
        archived_count = 0
        logger.log("Skipping archiving in low-memory mode")
    
    # Step 7: Update INDEX.md
    duration = int(time.time() - start_time)
    stats = {
        'duration': duration,
        'topics_updated': len(topic_map),
        'files_archived': archived_count,
        'active_projects': len(active_projects),
        'ram_status': ram_status,
        'ram_percent': ram_percent
    }
    
    logger.log("Updating INDEX.md...")
    if update_index(active_projects, topic_map, stats):
        logger.log("✅ INDEX.md updated successfully")
    else:
        logger.log("❌ Failed to update INDEX.md")
    
    # Step 8: Send notification
    logger.log("Sending notification...")
    send_notification(stats)
    
    logger.log(f"Distillation completed in {duration}s")
    logger.log("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Distillation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)
