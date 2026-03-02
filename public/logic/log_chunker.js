// Micro-Task 3.2: Context Window Management
// This logic will be used in n8n Code Node to balance log size and relevance

const MAX_TOKENS_EST = 100000; // Keep well within Gemini 128k
const logs = items[0].json.logs; // Assuming input is { logs: "..." }

function processLogs(rawLogs) {
    // 1. Identify Priority Actions (Actionable logs)
    const priorityKeywords = ["error", "fix", "decision", "preference", "goal", "update"];
    const lines = rawLogs.split('\n');
    
    let priorityLines = [];
    let generalLines = [];
    
    lines.forEach(line => {
        const lowerLine = line.toLowerCase();
        if (priorityKeywords.some(kw => lowerLine.includes(kw))) {
            priorityLines.push(line);
        } else {
            generalLines.push(line);
        }
    });

    // 2. Balance Strategy
    // Always keep all priority logs, then fill with recent general logs
    let finalLogs = [...priorityLines];
    let remainingSpace = MAX_TOKENS_EST - JSON.stringify(finalLogs).length;
    
    // Add general logs from the end (most recent) until limit
    for (let i = generalLines.length - 1; i >= 0; i--) {
        if (JSON.stringify(generalLines[i]).length < remainingSpace) {
            finalLogs.unshift(generalLines[i]);
            remainingSpace -= JSON.stringify(generalLines[i]).length;
        } else {
            break;
        }
    }

    return finalLogs.join('\n');
}

return [{ json: { processedLogs: processLogs(logs) } }];
