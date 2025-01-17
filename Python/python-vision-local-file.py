from openai import AzureOpenAI
import os
from dotenv import load_dotenv
import base64
from mimetypes import guess_type

#Sets the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

# Path of the image to be analyzed.
image_path = ''
imagedata = base64.b64encode(open(image_path, 'rb').read()).decode('ascii')

#Create Azure client
client = AzureOpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  
    api_version=os.environ['API_VERSION'],
    azure_endpoint = os.environ['OPENAI_API_BASE'],
    organization = os.environ['OPENAI_ORGANIZATION']
)
# print(data_url)
#Create Query
messages=[
        {"role": "system", "content": "As an AI tool specialized in image recognition, you will be given an image and asked to answer a question about it."},
        {"role": "user", "content": [
            {"type": "text", "text": "How many green dots are there?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/jpeg;base64,{imagedata}"}}
        ]}
    ]

response = client.chat.completions.create(
    model=os.environ['MODEL'],
    messages=messages,
    temperature=0.0,
)


#Print response.
print(response.choices[0].message.content)
