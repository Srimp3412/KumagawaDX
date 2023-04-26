import requests
import json
from utils.get_data import get_url

def create_single_text_message(message):
    kumagawa = ['uehara-bashi', 'hiate', 'ooiwa-yama', 'ooiwa-kawa', 'ebirase-kumagawa', 'ebirase-kawaguti']
    if message in kumagawa:
        message = get_url(message)

    test_message = [
                {
                    'type': 'text',
                    'text': message,
                }
            ]
    return test_message

def test(message):

    test_message = [
                {
                    'type': 'text',
                    'text': message,
                }
            ]
    return test_message