import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from dotenv import load_dotenv

load_dotenv('config.sh')

AZURE_AI_LANGUAGE_KEY      = os.getenv('AZURE_AI_LANGUAGE_KEY')
AZURE_AI_LANGUAGE_ENDPOINT = os.getenv('AZURE_AI_LANGUAGE_ENDPOINT')

def sample_recognize_pii_entities() -> None:
    
    text_analytics_client = TextAnalyticsClient(
        endpoint=AZURE_AI_LANGUAGE_ENDPOINT, credential=AzureKeyCredential(AZURE_AI_LANGUAGE_KEY)
    )
    documents = [
        """Parker Doe has repaid all of their loans as of 2020-04-25.
        Their SSN is 859-98-0987. To contact them, use their phone number
        555-555-5555. They are originally from Brazil and have Brazilian CPF number 998.214.865-68"""
    ]

    result = text_analytics_client.recognize_pii_entities(documents)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        print(f"Document text: {documents[idx]}")
        print(f"Redacted document text: {doc.redacted_text}")
        for entity in doc.entities:
            print("...Entity '{}' with category '{}' got redacted".format(
                entity.text, entity.category
            ))

    # [END recognize_pii_entities]

    social_security_numbers = []
    for doc in docs:
        for entity in doc.entities:
            if entity.category == 'USSocialSecurityNumber' and entity.confidence_score >= 0.6:
                social_security_numbers.append(entity.text)

if __name__ == '__main__':
    sample_recognize_pii_entities()
