import json

config_path = '/root/.openclaw/openclaw.json'

with open(config_path, 'r') as f:
    config = json.load(f)

topics = config['channels']['telegram']['groups']['-1003843376924']['topics']

# Remove old topics
old_topics = ["12", "78", "367"]
for t_id in old_topics:
    if t_id in topics:
        del topics[t_id]

with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)

print("Old topics removed from config.")
