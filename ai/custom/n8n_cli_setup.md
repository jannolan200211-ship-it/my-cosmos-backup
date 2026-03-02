# n8n CLI Tool (Cosmos Team)

n8n API ကို command line ကနေ လွယ်လွယ်ကူကူ အသုံးပြုနိုင်ဖို့အတွက် `scripts/n8n_api.py` ကို တည်ဆောက်ထားပါတယ်။

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- Environment Variables:
  - `N8N_API_KEY`: သင်၏ n8n API Key
  - `N8N_BASE_URL`: n8n ၏ Base URL (ဥပမာ- https://n8n.yourdomain.com)

## Usage Examples

### List Workflows
```bash
python3 scripts/n8n_api.py list-workflows
python3 scripts/n8n_api.py list-workflows --active true
```

### Activate/Deactivate Workflow
```bash
python3 scripts/n8n_api.py activate --id <id>
python3 scripts/n8n_api.py deactivate --id <id>
```

### List Executions
```bash
python3 scripts/n8n_api.py list-executions --limit 10
```

### Execute Workflow Manually
```bash
python3 scripts/n8n_api.py execute --id <id> --data '{"key": "value"}'
```

---

## Advance n8n Client (`scripts/n8n_client.py`)

Nolan ပေးထားတဲ့ ပိုမိုပြည့်စုံတဲ့ Client ဖြစ်ပါတယ်။ Workflow creation, validation နဲ့ statistics တွေပါ လုပ်ဆောင်နိုင်ပါတယ်။

### Usage Examples

```bash
python3 scripts/n8n_client.py list-workflows --pretty
python3 scripts/n8n_client.py stats --id <id> --pretty
python3 scripts/n8n_client.py validate --id <id> --pretty
```

---

## n8n Workflow Optimizer (`scripts/n8n_optimizer.py`)

n8n Workflows တွေရဲ့ Performance ကို Analyze လုပ်ဖို့နဲ့ ပိုကောင်းအောင် ဘယ်လိုပြင်ရမလဲဆိုတဲ့ Suggestions တွေထုတ်ပေးဖို့ အသုံးပြုပါတယ်။

### Usage Examples

```bash
# Workflow တစ်ခုလုံးကို Analyze လုပ်ပြီး Report ထုတ်ကြည့်ရန်
python3 scripts/n8n_optimizer.py report --id <id>

# Optimization suggestions များကြည့်ရန်
python3 scripts/n8n_optimizer.py suggest --id <id> --pretty
```

---

## n8n Workflow Tester (`scripts/n8n_tester.py`)

Workflow တွေကို အသက်မသွင်းခင် (Activate မလုပ်ခင်) စမ်းသပ်စစ်ဆေးဖို့နဲ့ Test cases တွေနဲ့ Run ကြည့်ဖို့ အသုံးပြုပါတယ်။

### Usage Examples

```bash
# Workflow ကို Validate လုပ်ပြီး Report ထုတ်ကြည့်ရန်
python3 scripts/n8n_tester.py validate --id <id> --report

# Test data နဲ့ Dry-run လုပ်ကြည့်ရန်
python3 scripts/n8n_tester.py dry-run --id <id> --data '{"test": "input"}' --report

# Test suite (multiple test cases) နဲ့ စစ်ဆေးရန်
python3 scripts/n8n_tester.py test-suite --id <id> --test-suite tests/workflow_tests.json
```

---
*Created by David (Manager) for Cosmos Team*
