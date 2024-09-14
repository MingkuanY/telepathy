## Abilities

### Communicate Covertly
Talk to another TELEPATHY device wearer without anybody knowing you are communicating!

### Image Visualizer
Describe your "thoughts" to a Flux model (hosted by Baseten). A picture is generated as if you were visualizing an image in your head.

See `baseten_genImage.py`.
Input: A string describing your image.
Output: Image in `flux.png`.

### Covert Ask LLM
Query llama without the outside world knowing.

See `covert_llm.py`.
Input: a string that is your query.
Output: Audio response in file `output_llm.mp3`, and optional text version of the restponse.


### Login - Quant WIP
For the paranoid privacy people. Nobody will see you type your password. Integrated with Clerk Sign-In.

### Capital One Banking Data
You can create a deposit or show all deposits. Nobody can see you enter bank information ever again.

**Create deposit**: `capitalOne_deposit.py`
Input: `amount` and `description`
Output: Success message "You have successfully created a deposit"

**Show deposits**: `capitalOne_deposit.py`
Input: `amount` and `description`
Output: Printout showing all deposits, each with fields: `transaction_date`, `amount`, `description`


Sample Data:
Customer # - Name - Account #
66e5fdea9683f20dd5189bd3 - Alex - 66e601b79683f20dd5189be3 (Credit Card)
66e5fec49683f20dd5189bd6 - Mingkuan
66e5fef29683f20dd5189bd9 - Kot
66e5ff1e9683f20dd5189bdb - Pranab



### Sing a Song with Suno - TODO
By default, generate a happy birthday song to expressively celebrate, even without the ability to vocalize audibly. You can also describe any song you would like to generate (ie. "Happy pop song about hacking")

Potentially in the future: use tongue clicks to indicate desired BPM for more custom song.

Input: "D" for default, or string descriptor of song.
Output: mp3
