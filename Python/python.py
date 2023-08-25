import openai
from dotenv import dotenv_values

#Load environment file for secrets.
secrets = dotenv_values(".env")  

# Send a completion call to generate an answer
print('Sending a test completion job')

#Define parameters and ask a query.
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

#Print response.
print(response['choices'][0]['message']['content'])