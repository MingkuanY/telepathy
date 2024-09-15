## API Keys
ElevenLabs: sk_edd71416ad1a81f444fb057e235b62f3a61dbec817e4089e

## Abilities
### Key
*Telepathize "s" to trigger these special abilities.*

1. Weather Lookup via TuneHQ: w 

1. News Summary via TuneHQ: n

1. Tell me a joke: j

1. Capital One Banking Show Deposits: s

1. Capital One Banking Create Deposit: c + amount, description (optional)

1. Image Visualizer: i + User Description

1. Covert Ask LLM via BaseTen: l + User Question

1. Whois? Lookup New Acquaintances via TuneHQ: a + User Question





### Communicate Covertly
Talk to another TELEPATHY device wearer without anybody knowing you are communicating!

### Image Visualizer
Describe your "thoughts" to a Flux model (hosted by Baseten). A picture is generated as if you were visualizing an image in your head.

See `baseten_genImage.py`.
Input: A string describing your image.
Output: Image in `flux.png`.

### Covert Ask LLM via BaseTen
Query llama without the outside world knowing.

See `covert_llm.py`.
Input: a string that is your query.
Output: Audio response in file `output_llm.mp3`, and optional text version of the restponse.

Requires: elevenlabs API key


### Capital One Banking Data
You can create a deposit or show all deposits. Nobody can see you enter bank information ever again.

**Create deposit**: `capitalOne_deposit.py`
Input: `amount` and `description`
Output: Success message "You have successfully created a deposit"

**Show deposits**: `capitalOne_deposit.py`
Output: Printout showing all deposits, each with fields: `transaction_date`, `amount`, `description`


Sample Data:
Customer # - Name - Account #
66e5fdea9683f20dd5189bd3 - Alex - 66e601b79683f20dd5189be3 (Credit Card)
66e5fec49683f20dd5189bd6 - Mingkuan
66e5fef29683f20dd5189bd9 - Kot
66e5ff1e9683f20dd5189bdb - Pranab


### Whois? Lookup New Acquaintances via TuneHQ
TuneHQ assistant performs google search on the requested person. See `tune.py`.

Input: First and last name
Output: Text description with short audio summary

Requires: Elevenlabs API key, TuneHQ API key

### Weather Lookup via TuneHQ
Requires: Elevenlabs API key, TuneHQ API key
See `tune_weather.py`.

### News Summary via TuneHQ
Requires: Elevenlabs API key, TuneHQ API key
See `tune_news.py`.

### Joke via TuneHQ
Requires: Elevenlabs API key, TuneHQ API key
See `tune_joke.py`.