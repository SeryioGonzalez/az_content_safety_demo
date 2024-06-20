import os

from azure.ai.contentsafety import BlocklistClient, ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import ( AddOrUpdateTextBlocklistItemsOptions, AnalyzeTextOptions, TextBlocklist, TextBlocklistItem)
from azure.core.exceptions import HttpResponseError
from dotenv import load_dotenv

load_dotenv('config.sh')

AZURE_CONTENT_SAFETY_KEY      = os.getenv('AZURE_CONTENT_SAFETY_KEY')
AZURE_CONTENT_SAFETY_ENDPOINT = os.getenv('AZURE_CONTENT_SAFETY_ENDPOINT')

# Create a Blocklist client
az_blocklist_client      = BlocklistClient(AZURE_CONTENT_SAFETY_ENDPOINT, AzureKeyCredential(AZURE_CONTENT_SAFETY_KEY))
az_content_sagety_client = ContentSafetyClient(AZURE_CONTENT_SAFETY_ENDPOINT, AzureKeyCredential(AZURE_CONTENT_SAFETY_KEY))

blocklist_name = "ateam"
blocklist_description = "Blocklist for the A-Team"
blocklist_text_list = [
    "hannibal",
    "ateam",
    "BA Baracus"
]

blocklist_items = [TextBlocklistItem(text=blocklist_text, description="String") for blocklist_text in blocklist_text_list]

input_text = "The ateam are criminals and must go jail"

try:
    blocklist = az_blocklist_client.create_or_update_text_blocklist(
        blocklist_name=blocklist_name,
        options=TextBlocklist(blocklist_name=blocklist_name, description=blocklist_description),
    )
    if blocklist:
        print(f"Blocklist created or updated. Name: {blocklist.blocklist_name}, Description: {blocklist.description}\n")
except HttpResponseError as e:
    print("\nCreate or update text blocklist failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise


print(f"Adding blocklist items to the blocklist {blocklist_name}...")
try:
    result = az_blocklist_client.add_or_update_blocklist_items(
        blocklist_name=blocklist_name, options=AddOrUpdateTextBlocklistItemsOptions(blocklist_items=blocklist_items))
except HttpResponseError as e:
    print("\nAdd blocklistItems failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise



try:
    # After you edit your blocklist, it usually takes effect in 5 minutes, please wait some time before analyzing
    # with blocklist after editing.
    analysis_result = az_content_sagety_client.analyze_text(
        AnalyzeTextOptions(text=input_text, blocklist_names=[blocklist_name], halt_on_blocklist_hit=False)
    )
    if analysis_result and analysis_result.blocklists_match:
        print("\nBlocklist match results: ")
        for match_result in analysis_result.blocklists_match:
            print(
                f"  BlocklistName: {match_result.blocklist_name}, BlocklistItemId: {match_result.blocklist_item_id}, "
                f"  BlocklistItemText: {match_result.blocklist_item_text}"
            )
except HttpResponseError as e:
    print("\nAnalyze text failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise