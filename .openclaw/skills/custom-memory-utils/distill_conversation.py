#!/usr/bin/env python3
"""
distill_conversation.py - Main orchestrator for conversation distillation

This script implements the 4-phase compact framework workflow:
1. Search First (ripgrep-based memory search)
2. Resource Awareness (RAM check and AI selection)
3. Distillation Logic (80/20 rule)
4. Multi-layered Storage (Hot/Warm/Cold updates)
"""

import os
import sys
import json
import subprocess
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Configuration
MEMORY_DIR = Path("/root/.openclaw/memory")
TOPICS_DIR = MEMORY_DIR / "topics"
INDEX_FILE = MEMORY_DIR / "INDEX.md"
SIGNALS_DIR = Path("/root/.openclaw/.signals")

class ConversationDistiller:
    def __init__(self, thread_id: str, conversation: List[Dict]):
        self.thread_id = thread_id
        self.conversation = conversation
        self.distilled_content = None
        self.topic_name = None
        self.ai_mode = None
        
    def run_full_workflow(self):
        """Execute all 4 phases of distillation"""
        print("=" * 60)
        print("COMPACT FRAMEWORK - Conversation Distillation")
        print("=" * 60)
        
        # Phase 1: Search First
        print("\n[Phase 1: Search First]")
        existing_memory = self.search_existing_memory()
        
        # Phase 2: Resource Awareness
        print("\n[Phase 2: Resource Awareness]")
        self.ai_mode = self.check_resources()
        
        # Phase 3: Distillation Logic
        print("\n[Phase 3: Distillation Logic]")
        self.distilled_content = self.distill_conversation()
        
        # Phase 4: Multi-layered Storage
        print("\n[Phase 4: Multi-layered Storage]")
        self.update_storage()
        
        print("\n" + "=" * 60)
        print("✅ Distillation completed successfully")
        print("=" * 60)
        
    # ========== Phase 1: Search First ==========
    
    def search_existing_memory(self) -> Optional[Path]:
        """
        Use ripgrep to find existing memory files
        Returns path to existing memory file or None
        """
        print(f"🔍 Searching for existing memory (thread_id: {self.thread_id})...")
        
        # Search by thread_id
        try:
            result = subprocess.run(
                ['rg', '-l', f'thread_id: {self.thread_id}', str(TOPICS_DIR)],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0 and result.stdout.strip():
                existing_file = Path(result.stdout.strip().split('\n')[0])
                print(f"✅ Found existing memory: {existing_file.name}")
                return existing_file
            
        except Exception as e:
            print(f"⚠️  Ripgrep search failed: {e}")
        
        # Infer topic from conversation
        self.topic_name = self.infer_topic()
        print(f"📝 Inferred topic: {self.topic_name}")
        
        # Search by topic
        try:
            result = subprocess.run(
                ['rg', '-l', f'Topic: {self.topic_name}', str(TOPICS_DIR)],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0 and result.stdout.strip():
                existing_file = Path(result.stdout.strip().split('\n')[0])
                print(f"✅ Found topic file: {existing_file.name}")
                return existing_file
                
        except Exception as e:
            print(f"⚠️  Topic search failed: {e}")
        
        print("ℹ️  No existing memory found, will create new")
        return None
    
    def infer_topic(self) -> str:
        """Infer topic name from conversation content"""
        # Extract keywords from messages
        text = ' '.join([msg.get('content', '') for msg in self.conversation[:10]])
        
        # Simple keyword extraction (in production, use TF-IDF or LLM)
        keywords = re.findall(r'\b[a-z]{4,}\b', text.lower())
        
        # Common words to ignore
        stopwords = {'that', 'this', 'have', 'with', 'from', 'they', 'will', 'would'}
        keywords = [k for k in keywords if k not in stopwords]
        
        # Get top keywords
        from collections import Counter
        top_keywords = Counter(keywords).most_common(3)
        
        if top_keywords:
            topic = '-'.join([k[0] for k in top_keywords[:2]])
            return topic
        
        # Fallback
        return f"thread-{self.thread_id[:8]}"
    
    # ========== Phase 2: Resource Awareness ==========
    
    def check_resources(self) -> str:
        """
        Check available RAM and select appropriate AI mode
        Returns: 'cloud', 'local_streaming', or 'local_full'
        """
        print("💾 Checking RAM availability...")
        
        try:
            result = subprocess.run(
                ['free', '-m'],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Parse output
            lines = result.stdout.strip().split('\n')
            mem_line = lines[1].split()
            total_ram = int(mem_line[1])
            used_ram = int(mem_line[2])
            available_ram = int(mem_line[6])
            
            print(f"   Total: {total_ram}MB")
            print(f"   Used: {used_ram}MB")
            print(f"   Available: {available_ram}MB")
            
            # Decide AI mode
            if available_ram < 200:
                print("⚠️  LOW RAM: Will use Gemini API (cloud)")
                return 'cloud'
            elif available_ram < 500:
                print("⚡ MODERATE RAM: Will use local AI with streaming")
                return 'local_streaming'
            else:
                print("✅ SUFFICIENT RAM: Will use local AI (full)")
                return 'local_full'
                
        except Exception as e:
            print(f"❌ Error checking RAM: {e}")
            print("Defaulting to cloud mode")
            return 'cloud'
    
    # ========== Phase 3: Distillation Logic ==========
    
    def distill_conversation(self) -> str:
        """
        Apply 80/20 rule distillation based on selected AI mode
        """
        print(f"🔄 Distilling conversation using {self.ai_mode} mode...")
        
        # Classify messages by priority
        critical_msgs = self.extract_critical_messages()
        decisions = self.extract_decisions()
        tasks = self.extract_tasks()
        preferences = self.extract_preferences()
        
        print(f"   Critical messages: {len(critical_msgs)}")
        print(f"   Decisions found: {len(decisions)}")
        print(f"   Tasks found: {len(tasks)}")
        print(f"   Preferences found: {len(preferences)}")
        
        # Format distilled output
        distilled = self.format_distilled_output(
            critical_msgs, decisions, tasks, preferences
        )
        
        # Validate
        if self.validate_distillation(distilled):
            print("✅ Distillation validated successfully")
            return distilled
        else:
            print("⚠️  Distillation validation failed, using emergency mode")
            return self.emergency_distillation()
    
    def extract_critical_messages(self) -> List[Dict]:
        """Extract TIER 1 messages (must retain)"""
        critical = []
        
        for msg in self.conversation:
            content = msg.get('content', '')
            
            # Check for tags
            if any(tag in content for tag in ['#IMPORTANT', '#URGENT', '#TODO']):
                critical.append(msg)
                continue
            
            # Check for decision keywords
            if any(kw in content.lower() for kw in [
                'decided', 'agreed', 'will do', 'must', 'should', 'action:', 'decision:'
            ]):
                critical.append(msg)
                continue
            
            # Check for task markers
            if '[ ]' in content or '[x]' in content:
                critical.append(msg)
                continue
        
        return critical
    
    def extract_decisions(self) -> List[str]:
        """Extract explicit decisions"""
        decisions = []
        
        for msg in self.conversation:
            content = msg.get('content', '')
            
            # Look for decision patterns
            if re.search(r'(decided|agreed|will|must).*:', content, re.I):
                decisions.append(content)
            
            if 'DECISION:' in content.upper():
                decisions.append(content)
        
        return decisions
    
    def extract_tasks(self) -> List[Dict]:
        """Extract tasks with status"""
        tasks = []
        
        for msg in self.conversation:
            content = msg.get('content', '')
            
            # Find task patterns
            task_matches = re.findall(r'(\[[ x]\])\s+(.+?)(?:\n|$)', content)
            
            for status_marker, task_desc in task_matches:
                tasks.append({
                    'description': task_desc.strip(),
                    'status': 'done' if '[x]' in status_marker else 'pending',
                    'timestamp': msg.get('timestamp', '')
                })
        
        return tasks
    
    def extract_preferences(self) -> List[str]:
        """Extract user preferences"""
        preferences = []
        
        for msg in self.conversation:
            content = msg.get('content', '')
            sender = msg.get('sender', '')
            
            # Only from Nolan
            if sender.lower() != 'nolan':
                continue
            
            # Look for preference patterns
            if any(indicator in content for indicator in [
                'I prefer', 'I want', 'Always', 'Never', 'Make sure', 'Remember'
            ]):
                preferences.append(content)
        
        return preferences
    
    def format_distilled_output(self, critical_msgs, decisions, tasks, preferences) -> str:
        """Format into required structure"""
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        output = f"""# {self.topic_name.replace('-', ' ').title()}

**Metadata:**
- Topic: {self.topic_name}
- Thread ID: {self.thread_id}
- Date: {now}
- Original Messages: {len(self.conversation)}
- Distilled Messages: {len(critical_msgs)}
- Compression: {len(critical_msgs) / len(self.conversation) * 100:.1f}%

---

## [Core Logic/Decision]

"""
        # Add decisions
        if decisions:
            output += "### Key Decisions\n\n"
            for i, decision in enumerate(decisions[:5], 1):
                output += f"{i}. {decision}\n\n"
        
        # Add preferences
        if preferences:
            output += "### Preferences (Nolan)\n\n"
            for pref in preferences:
                output += f"- {pref}\n"
            output += "\n"
        
        output += "---\n\n## [Active Tasks]\n\n"
        
        # Add tasks
        if tasks:
            for task in tasks:
                status_marker = '[x]' if task['status'] == 'done' else '[ ]'
                output += f"{status_marker} {task['description']}\n"
                output += f"  - Status: {task['status'].title()}\n\n"
        else:
            output += "No active tasks identified.\n\n"
        
        output += "---\n\n## [Next Goals]\n\n"
        output += "### Immediate\n"
        output += "1. (To be determined based on context)\n\n"
        
        output += "---\n\n## [Reference Links]\n\n"
        output += f"- Original Thread: `openclaw.db/threads/{self.thread_id}`\n"
        
        return output
    
    def validate_distillation(self, distilled: str) -> bool:
        """Validate that distillation meets requirements"""
        # Check for required sections
        required_sections = [
            '[Core Logic/Decision]',
            '[Active Tasks]',
            '[Next Goals]'
        ]
        
        for section in required_sections:
            if section not in distilled:
                print(f"⚠️  Missing required section: {section}")
                return False
        
        # Check compression ratio
        original_text = ' '.join([m.get('content', '') for m in self.conversation])
        if len(distilled) > len(original_text):
            print("⚠️  Distilled content is longer than original!")
            return False
        
        return True
    
    def emergency_distillation(self) -> str:
        """Fallback rule-based distillation"""
        print("🚨 Using emergency distillation mode")
        
        critical_msgs = self.extract_critical_messages()
        
        output = f"""# Emergency Distillation - {self.topic_name}

**Warning**: This is an emergency distillation using rule-based extraction.

## Critical Messages

"""
        for msg in critical_msgs[:20]:
            output += f"- {msg.get('content', '')}\n"
        
        return output
    
    # ========== Phase 4: Multi-layered Storage ==========
    
    def update_storage(self):
        """Update all three memory tiers"""
        print("💾 Updating multi-layered storage...")
        
        # Create directories if needed
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        TOPICS_DIR.mkdir(parents=True, exist_ok=True)
        SIGNALS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Tier 1: Update INDEX.md
        self.update_index_md()
        
        # Tier 2: Save to topics file
        self.save_to_warm_memory()
        
        # Tier 3: Signal for cold storage cleanup
        self.signal_cold_storage()
        
        print("✅ All tiers updated successfully")
    
    def update_index_md(self):
        """Update INDEX.md with new entry"""
        print("   [Tier 1] Updating INDEX.md...")
        
        # Create INDEX.md if doesn't exist
        if not INDEX_FILE.exists():
            INDEX_FILE.write_text("""# 📌 GLOBAL_KNOWLEDGE_INDEX

Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 🔥 ACTIVE_PROJECTS

## 📂 TOPIC_MAP

## ⏱️ LAST_DISTILLATION

""")
        
        # Read current content
        content = INDEX_FILE.read_text()
        
        # Add entry to TOPIC_MAP
        entry = f"- **{self.topic_name.title()}** → `memory/topics/{self.topic_name}.md` (Updated: {datetime.now().strftime('%Y-%m-%d')})\n"
        
        # Insert into TOPIC_MAP section
        if '## 📂 TOPIC_MAP' in content:
            parts = content.split('## 📂 TOPIC_MAP')
            if len(parts) == 2:
                # Check if entry already exists
                if self.topic_name not in parts[1].split('##')[0]:
                    parts[1] = '\n' + entry + parts[1]
                content = '## 📂 TOPIC_MAP'.join(parts)
        
        INDEX_FILE.write_text(content)
        print("   ✅ INDEX.md updated")
    
    def save_to_warm_memory(self):
        """Save distilled content to topic file"""
        print(f"   [Tier 2] Saving to topics/{self.topic_name}.md...")
        
        topic_file = TOPICS_DIR / f"{self.topic_name}.md"
        
        if topic_file.exists():
            # Append mode
            existing = topic_file.read_text()
            separator = f"\n\n---\n## Update: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            new_content = existing + separator + self.distilled_content
            topic_file.write_text(new_content)
            print(f"   ✅ Appended to existing file")
        else:
            # Create new
            topic_file.write_text(self.distilled_content)
            print(f"   ✅ Created new file")
    
    def signal_cold_storage(self):
        """Create signal for database cleanup"""
        print("   [Tier 3] Creating cleanup signal...")
        
        signal_file = SIGNALS_DIR / f"compact_{self.thread_id}.signal"
        
        signal_data = {
            'thread_id': self.thread_id,
            'action': 'archive',
            'reason': 'Distilled to Tier 2',
            'distilled_to': f'memory/topics/{self.topic_name}.md',
            'timestamp': datetime.now().isoformat(),
            'original_size': len(self.conversation),
            'compression_ratio': len(self.distilled_content) / sum(len(m.get('content', '')) for m in self.conversation)
        }
        
        signal_file.write_text(json.dumps(signal_data, indent=2))
        print(f"   ✅ Signal created")

def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print("Usage: python3 distill_conversation.py <thread_id> <conversation_json>")
        sys.exit(1)
    
    thread_id = sys.argv[1]
    conversation_file = sys.argv[2]
    
    # Load conversation
    with open(conversation_file) as f:
        conversation = json.load(f)
    
    # Run distillation
    distiller = ConversationDistiller(thread_id, conversation)
    distiller.run_full_workflow()

if __name__ == "__main__":
    main()
