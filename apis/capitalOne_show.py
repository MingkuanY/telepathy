import requests
import json

#QUERY DB FOR THIS INFO
card_id = "66e601b79683f20dd5189be3" #this is Alex's credit card


url = f"http://api.nessieisreal.com/accounts/{card_id}/deposits?key=2bc034cd8680c577516f30dfe52a67ff"

# Make the GET request
response = requests.get(url, headers={'Accept': 'application/json'})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and print it
    transactions = response.json()
    print(json.dumps(transactions, indent=4))
else:
    print(f"Failed to fetch transactions: {response.status_code}, {response.text}")
