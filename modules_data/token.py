import json

with open('data/server/token.json', 'r') as f:
    data = json.load(f)
    token = data['token'].strip()
