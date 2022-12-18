import os
import requests

webhook_url = 'https://discord.com/api/webhooks/1053866016679153684/f_DpGe-GT0kGVq08fzmowAC08wUJ6iL49q1B7gud9U0YqeQ4E7-37v8JGDMOPoEcMZZu'

search_dir = 'database'

search_term = input('Enter the search term: ')

results = []

for filename in os.listdir(search_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(search_dir, filename), 'r', encoding='utf-8') as txt_file:
            for line in txt_file:
                if search_term in line:
                    results.append(line)

if results:
    data = {'content': f'Databases results for "{search_term}":\n' + '\n'.join(results)}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print('Search results successfully sent to Discord webhook')