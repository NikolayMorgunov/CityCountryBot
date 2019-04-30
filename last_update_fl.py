import requests

def last_update(data):
    results = data['result']
    if results:
        total_updates = len(results) - 1
        return results[total_updates]
