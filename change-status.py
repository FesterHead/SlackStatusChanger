from random import randint
from datetime import datetime
import random
import os
from time import sleep
from slack_sdk import WebClient
from jproperties import Properties

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

tokens = Properties()
with open("slack-tokens.properties", "rb") as tokens_file:
    tokens.load(tokens_file)
tokens_view = tokens.items()

for token_item in tokens_view:
    client = WebClient(token=token_item[1].data)
    text = random_line('text.properties')
    emoji = random_line('emoji.properties')
    print('[{}] {} | {} | {}'.format(datetime.now(), token_item[0], emoji, text))
    response = client.api_call(
        api_method='users.profile.set',
        params={'profile': '{"status_text":"' + text + '","status_emoji":"' + emoji + '","status_expiration":0}'}
    )
