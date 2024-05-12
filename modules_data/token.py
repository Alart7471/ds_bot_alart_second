import json

with open('data/server/token.json', 'r') as f:
    data = json.load(f)
    bot_token = data['bot_token'].strip()
    openai_key = data['openai_key'].strip()
    vk_token = data['vk_token'].strip()
    group_id = data['group_id'].strip()