import os
import requests

webhook_url = input('Enter the webhook url: ')

search_dir = 'database'

search_term = input('Search: ')

results = []

for filename in os.listdir(search_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(search_dir, filename), 'r', encoding='utf-8') as txt_file:
            for line in txt_file:
                if search_term in line:
                    results.append(line)

if results:
    data = {
        'embeds': [{
            'title': f'Databases results for "{search_term}"',
            'description': '\n'.join(results),
            'footer': {
                'text': 'Database Searcher |  Made By Zin0vich.'
            }
        }]
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print('Search results successfully sent to Discord webhook')
