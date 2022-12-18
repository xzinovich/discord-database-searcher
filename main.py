import os
import requests
import threading
import concurrent.futures
import functools

webhook_url = input('Webhook Url: ')

search_dir = 'database'

search_term = input('Search: ')

results = set()

results_lock = threading.Lock()

@functools.lru_cache(maxsize=1024)
def read_file(filename):
    with open(os.path.join(search_dir, filename), 'r', encoding='utf-8') as txt_file:
        return txt_file.readlines()

def search_file(filename):
    lines = read_file(filename)
    for line in lines:
        if search_term in line:
            with results_lock:
                results.add(line)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for filename in os.listdir(search_dir):
        if filename.endswith('.txt') or filename.endswith('.csv') or filename.endswith('.sql'):
            # Create a new thread to search the file
            executor.submit(search_file, filename)

if results:
    data = {
        'embeds': [{
            'title': f'🔎 | Databases results for "{search_term}"',
            'description': '\n'.join(results),
            'color': 0xFF0000,
            'thumbnail': {
                'url': 'https://cdn.discordapp.com/attachments/1044567285085507584/1053993114051813466/image.png'
            },
            'fields': [
                {
                    'name': 'creator:',
                    'value': '``Made By xZin0vich#0105``'
                },
                {
                    'name': 'server:',
                    'value': '``discord.gg/overdrive``'
                },
            ],
            'footer': {
                'text': 'Database Searcher |  greetz to: zalko, kazuyaweb, wdb'
            }
        }]
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print('Search results successfully sent to Discord webhook')