# examples
A collection of code examples you can use to access the U-M GPT Toolkit API service.  

**Common required parameters**  
  
Note that these parameters may be represented by slightly differnt naming conventions, depepending on script language and module requirements.  
   
MODEL = Model names (gpt-35-turbo, gpt-4, gpt-4o, and etc)  
API gateway URL = "https://api.umgpt.umich.edu/azure-openai-api"    
API VERSION = " 2024-06-01" #latest non-preview completion version  
DEPLOYMENT_ID = "gpt-35-turbo" #chat deployment model name  
API_KEY #your 32 character API key  
ORGANIZATION #a valid 6 digit shortcode  

Please create a .env in the same directory as your script with the following:


MODEL=gpt-4o<br />
OPENAI_API_BASE=https://api.umgpt.umich.edu/azure-openai-api<br />
OPENAI_API_KEY=X<br />
OPENAI_ORGANIZATION=X<br />
API_VERSION=2024-06-01<br />


**References**  
  
[Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
