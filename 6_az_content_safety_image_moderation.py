import base64
import os
import requests

from dotenv import load_dotenv

# Configuration variables
load_dotenv('config.sh')

AZURE_CONTENT_SAFETY_KEY         = os.getenv('AZURE_CONTENT_SAFETY_KEY')
AZURE_CONTENT_SAFETY_ENDPOINT    = os.getenv('AZURE_CONTENT_SAFETY_ENDPOINT')
AZURE_CONTENT_SAFETY_API_VERSION = os.getenv('AZURE_CONTENT_SAFETY_API_VERSION')

# Encode the image to base64
image_file_path = 'medieval-knight.jpg'
with open(image_file_path, "rb") as image_file:
    image_base_64 = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare headers and data for the POST request
headers = {
    'Ocp-Apim-Subscription-Key': AZURE_CONTENT_SAFETY_KEY,
    'Content-Type': 'application/json'
}

data = {
    'image': {
        'content': image_base_64
    },
    'categories': ['Hate', 'Sexual', 'SelfHarm', 'Violence'],
    'outputType': 'FourSeverityLevels'
}

# Send the POST request
response = requests.post(f"{AZURE_CONTENT_SAFETY_ENDPOINT}/contentsafety/image:analyze?api-version={AZURE_CONTENT_SAFETY_API_VERSION}", json=data, headers=headers)

print(response.json())
