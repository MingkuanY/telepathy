#Use case: your imagination, visualize the thoughts in your head

import requests
import base64
import json

MODEL_ID = "7qk7m1dw"
BASETEN_API_KEY = "YMKFudUr.FcjOTi13DlaR3ZtCbBIumoXeqFJy25yx" # Paste from Discord

# Should take ~20 seconds, see link below for faster models

payload = {
    "prompt": "Giant concrete blocks that spell HACK MIT with the word 'HACK' on top of the word 'MIT' in a dense forest",
    "steps": 50
}

# Call model endpoint
res = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload
)

img_b64 = json.loads(res.text).get("data")
img = base64.b64decode(img_b64)

img_file = open("flux.png", "wb") # Note this will overwrite an existing flux.png file
img_file.write(img)
img_file.close()