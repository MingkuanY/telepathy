import requests

MODEL_ID = "03y55vew"
BASETEN_API_KEY = "YMKFudUr.FcjOTi13DlaR3ZtCbBIumoXeqFJy25yx" # Paste from Discord

payload = {
  "url": "https://cdn.baseten.co/docs/production/Gettysburg.mp3"
}


# Call model endpoint
res = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload
)

# Print the output of the model
print(res.json())
     