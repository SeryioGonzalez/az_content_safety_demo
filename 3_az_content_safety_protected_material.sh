source config.sh

MODE="text"
VERB="detectProtectedMaterial"

curl --location --request POST "$AZURE_CONTENT_SAFETY_ENDPOINT/contentsafety/$MODE:$VERB?api-version=$AZURE_CONTENT_SAFETY_API_VERSION" \
--header "Ocp-Apim-Subscription-Key: $AZURE_CONTENT_SAFETY_KEY" \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "to everyone, the best things in life are free. the stars belong to everyone, they gleam there for you and me. the flowers in spring, the robins that sing, the sunbeams that shine, they are yours, they are mine. and love can come to everyone, the best things in life are"
}'

