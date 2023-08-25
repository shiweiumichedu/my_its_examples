from langchain.schema import HumanMessage
from langchain.chat_models import AzureChatOpenAI
#import logging
from dotenv import dotenv_values
import os

secrets = dotenv_values(".env")  #Load environment file for secrets.

llm = AzureChatOpenAI(
    deployment_name=secrets['model'],
    openai_api_version=secrets['API_VERSION'],
    openai_api_key=secrets['OPENAI_API_KEY'],
    openai_api_base=secrets['openai_api_base'],
    openai_organization=secrets['OPENAI_organization']
    )
msg = HumanMessage(content="Explain step by step. Where is the University of Michigan?")
print(llm(messages=[msg]))
