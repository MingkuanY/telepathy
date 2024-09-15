import base64
import requests
import os

# Replace the empty string with your model id below
model_id = "" #TODO idk what this is but it doesn't work rn
#oh i think i have to like deploy it on a container thats a lot of work!

baseten_api_key = "YMKFudUr.FcjOTi13DlaR3ZtCbBIumoXeqFJy25yx"
BASE64_PREAMBLE = "data:image/png;base64,"

data = {
    "prompt": "a picture of a rhino wearing a suit",
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
img_b64 = res.get("result")
img = base64.b64decode(img_b64)

# Save the base64 string to a PNG
img_file = open("sdxl-output-1.png", "wb")
img_file.write(img)
img_file.close()
os.system("open sdxl-output-1.png")