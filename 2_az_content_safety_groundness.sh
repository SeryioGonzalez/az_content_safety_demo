source config.sh

MODE="text"
VERB="detectGroundedness"

curl --location --request POST "$AZURE_CONTENT_SAFETY_ENDPOINT/contentsafety/$MODE:$VERB?api-version=$AZURE_CONTENT_SAFETY_API_VERSION" \
--header "Ocp-Apim-Subscription-Key: $AZURE_CONTENT_SAFETY_KEY" \
--header 'Content-Type: application/json' \
--data-raw '{
  "domain": "Generic",
  "task": "QnA",
  "qna": {
       "query": "How much does she currently get paid per hour at the bank?"
  },
  "text": "12/hour",
  "groundingSources": [
    "I am 21 years old and I need to make a decision about the next two years of my life. Within a week. I currently work for a bank that requires strict sales goals to meet. IF they are not met three times (three months) you are canned. They pay me 10/hour and it is not unheard of to get a raise in 6ish months. The issue is, I am not a salesperson. That is not my personality. I am amazing at customer service, I have the most positive customer service reports done about me in the short time I have worked here. A coworker asked do you ask for people to fill these out? you have a ton. That being said, I have a job opportunity at Chase Bank as a part time teller. What makes this decision so hard is that at my current job, I get 40 hours and Chase could only offer me 20 hours/week. Drive time to my current job is also 21 miles **one way** while Chase is literally 1.8 miles from my house, allowing me to go home for lunch. I do have an apartment and an awesome roommate that I know wont be late on his portion of rent, so paying bills with 20hours a week is not the issue. It is the spending money and being broke all the time. I previously worked at Wal-Mart and took home just about 400 dollars every other week. So I know i can survive on this income. I just do not know whether I should go for Chase as I could definitely see myself having a career there. I am a math major likely going to become an actuary, so Chase could provide excellent opportunities for me **eventually**."
  ],
  "reasoning": false
}'

