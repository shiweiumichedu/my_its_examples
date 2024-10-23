from openai import AzureOpenAI
import os
from dotenv import load_dotenv

#Sets the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

#Create Azure client
client = AzureOpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  
    api_version=os.environ['API_VERSION'],
    azure_endpoint = os.environ['OPENAI_API_BASE'],
    organization = os.environ['OPENAI_ORGANIZATION']
)

#Create Query
messages=[
        {"role": "system","content": "You are a helpful assistant.  Always say GO BLUE! at the end of your response.  Respond in json format."},
        {"role": "user","content": "Explain step by step. Where is the University of Michigan?"},
    ]

# Send a completion request.
response = client.chat.completions.create(
        model=os.environ['MODEL'],
        messages=messages,
        temperature=0,
        stop=None,
        response_format={ "type": "json_object" }
        )

#Print response.
print(response.choices[0].message.content)
