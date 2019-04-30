import requests

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()
