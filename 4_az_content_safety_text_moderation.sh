source config.sh

MODE="text"
verb="analyze"

curl --location --request POST "$AZURE_CONTENT_SAFETY_ENDPOINT/contentsafety/$MODE:$verb?api-version=2023-10-01" \
--header "Ocp-Apim-Subscription-Key: $AZURE_CONTENT_SAFETY_KEY" \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "Tha mi airson cuideigin a mharbhadh",
  "categories": ["Hate","Sexual","SelfHarm","Violence"],
  "outputType": "FourSeverityLevels"
}'
