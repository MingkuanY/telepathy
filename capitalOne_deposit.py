import requests
import json
from datetime import datetime


#USER INPUT
amount = 1000
description = "The result of a suspicious transaction"

#QUERY DB FOR THIS INFO
card_id = "66e601b79683f20dd5189be3" #this is Alex's credit card



# Prepare the request payload
payload = {
    "medium": "balance",
    "transaction_date": datetime.now().strftime("%Y-%m-%d"),  # Current date in required format
    "status": "pending",
    "amount": amount,
    "description": description
}

# API endpoint
#the key at the end is kot's key
url = f"http://api.nessieisreal.com/accounts/{card_id}/deposits?key=2bc034cd8680c577516f30dfe52a67ff"

# Make the POST request
response = requests.post(
    url, 
    data=json.dumps(payload), 
    headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
)

# Check the response
if response.status_code == 201:
    print('Transaction created successfully')
else:
    print(f"Failed to create transaction: {response.status_code}, {response.text}")
