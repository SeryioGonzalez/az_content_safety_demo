import os
import requests

from dotenv import load_dotenv

# Configuration variables
load_dotenv('config.sh')

AZURE_OPENAI_API_KEY     = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT    = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")

SYSTEM_PROMPT  = """
###### MODEL ROLE #######
You are an expert hidding Personal information. 
###### DESIRED RESPONSE FORMAT AND STYLE #######
Respond with the input text, but hide any personal information you find. Also the name of any corporation or organization you find.
###### OUTPUT EXAMPLES #######
Examples: "My name is John Doe, and my phone number is 555-555-5555" should be redacted to "My name is [NAME], and my phone number is [PHONE]"
"Pedro vive en Madrid y su número de teléfono es 656777777" should be redacted to "Pedro vive en [LOCATION] y su número de teléfono es [PHONE]"
"""

CUSTOMER_INPUT = """Parker Doe has repaid all of their loans as of 2020-04-25.
        Their SSN is 859-98-0987. To contact them, use their phone number
        555-555-5555. They are originally from Brazil and have Brazilian CPF number 998.214.865-68"""

CUSTOMER_INPUT = """
Chory Pedro Martinez ma 68 lat i cierpi na chorobę serca. Ma cukrzycę. Jego numer telefonu to 656777777 i mieszka pod adresem 76 Serrano Street w Madrycie.

"""

az_openai_url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview"
headers = {'api-key': AZURE_OPENAI_API_KEY, 'Content-Type': 'application/json'}

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user",   "content": CUSTOMER_INPUT}
]
data={"messages": messages}
response = requests.post(az_openai_url, headers=headers, json=data)

print(response.json()['choices'][0]['message']['content'])