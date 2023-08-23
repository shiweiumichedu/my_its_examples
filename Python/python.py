import openai
#import logging
from dotenv import dotenv_values
import os

secrets = dotenv_values(".env")  #Load environment file for secrets.
#logging.basicConfig(level=logging.DEBUG)


# Send a completion call to generate an answer
print('Sending a test completion job')

response = openai.ChatCompletion.create(
      api_key = secrets['OPENAI_API_KEY'],
      organization = secrets['OPENAI_organization'],
      api_base= secrets['openai_api_base'],
      api_type = secrets['openai_api_type'],
      api_version = secrets['API_VERSION'],
      engine = secrets['model'],
      messages = [{"role":"system","content":"You are a helpful ” \
        “bot"},{"role":"user","content":"What is 2+2"}],
      temperature=0,
      max_tokens=500,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
#print(response('content'))
print(response)
print(response['choices'][0]['message']['content'])