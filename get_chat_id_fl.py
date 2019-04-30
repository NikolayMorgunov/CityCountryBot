import requests

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id
