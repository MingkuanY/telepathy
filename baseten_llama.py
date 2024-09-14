# Setup

import requests

user_query = "Turn the following letters into space separated words: hellomynameiskot"

MODEL_ID = "8w6yyp2q" #LLAMA
BASETEN_API_KEY = "YMKFudUr.FcjOTi13DlaR3ZtCbBIumoXeqFJy25yx" # Paste from Discord

messages = [
    {"role": "system", "content": "You are an expert software developer serving as a mentor at the HackMIT hackathon."},
    {"role": "user", "content": user_query},
]

payload = {
    "messages": messages,
    "stream": True,
    "max_new_tokens": 2048,
    "temperature": 0.9
}

# Call model endpoint
res = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
    stream=True
)

# Print the generated tokens as they get streamed
for content in res.iter_content():
    print(content.decode("utf-8"), end="", flush=True)