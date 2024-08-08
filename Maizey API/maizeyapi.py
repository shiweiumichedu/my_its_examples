import requests
import os
from dotenv import load_dotenv
import json

# To use this demo, please start by creating a .env file with your token.
# It should have a single line of the form
# token = "TOKEN_GOES_HERE"
# (Without the commenting #, though!)

# Then, replace project_pk below with your project GUID, accessible through the Maizey dashboard -> Project Detail.

# You can find the full API specification at https://umgpt.umich.edu/api/schema-public/swagger-ui/

url = 'https://umgpt.umich.edu'
project_pk = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
# REPLACE THE ABOVE project_pk WITH YOUR MAIZEY GUID! #

# Attempts to load in your .env file, which should be in the same directory as this notebook.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

# These are the basic headers used in every Maizey request. They shouldn't change.
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + os.environ['token'],
    'Content-Type': 'application/json'
}

# This is the endpoint for creating new conversations.
new_convo = f'{url}/maizey/api/projects/{project_pk}/conversation/'

# When creating a conversation, the json should always be empty.
response = requests.post(new_convo, headers=headers, json={})

print(response.json())

# First, we pull the conversation_pk from the conversation we just created.
conversation_pk = response.json()["pk"]

# This is the endpoint for creating new messages.
new_msg = f'{url}/maizey/api/projects/{project_pk}/conversation/{conversation_pk}/messages/'

# You can replace the query with whatever you'd like.
response = requests.post(new_msg, headers=headers, json={
    "query": "Hello, who are you and what can you do?"
})

# While this example only shows the response, you can also pull sources!
print(response.json()['response'])