source config.sh

MODE="text"
VERB="incidents"

curl --location --request PATCH "$AZURE_CONTENT_SAFETY_ENDPOINT/contentsafety/$MODE/$VERB/my-incident?api-version=$AZURE_CONTENT_SAFETY_API_VERSION" \
--header "Ocp-Apim-Subscription-Key: $AZURE_CONTENT_SAFETY_KEY" \
--header 'Content-Type: application/json' \
--data '{
  "incidentName": "my-incident",
  "incidentDefinition": "string"
}'

