import openai
import os
from helpers import add_now, sleep_if_needed

###############################################################################
# A Medium article that describes this project is here:
# https://medium.com/@real.zyxxy/using-chatgpt-to-review-tiny-python-snippets-6f236d689858

###############################################################################
# do change these values - they are the parameters of ChatGPT request
###############################################################################

prompts = ["""Could you optimise the following code:

n = int(input())
li = [i*i for i in range(n)]
print(li[0:n])""",
           
          """Could you review  the following code:

n = int(input())
assert n >= 0
li = [i*i for i in range(n)]
print(li[0:n])""",
           
          """First, forget the previous code reviews. 

Second, could you review the following code:

n = int(input())
li = [i*i for i in range(n)]
print(li[0:n])""",
           
          """First, forget the previous code reviews. 

Second, could you optimise the following code:
n = int(input())
li = [i*i for i in range(n)]
print(li[0:n])"""]  # That's your chat prompt
# You can change its value - ask ChatGPT anything you like.

temperature = 0.9  # temperature's value must be a number between 0.0 and 1.0,
# 0.0 being the most deterministic, consistent ChatGPT mode,
# and 1.0 being the most randon, unpredictable, creative ChatGPT mode.

###############################################################################
# technical part - it informs the package about your OpenAI API key
###############################################################################
# you need to get your personal OpenAI API key,
# then assign its value to
# a secret (system variable) OPENAI_API_KEY.
# It will only take a few minutes, and there is no need to pay money,
# or share your bank card details.
# Then, save it as a secret named OPENAI_API_KEY . Instructions here ->
# https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables

if "OPENAI_API_KEY" not in os.environ:
  raise Exception(
    "You need to assign your your OpenAI API key to system variable (Replit's secret) named 'OPENAI_API_KEY'. It will only take a few minutes, and there is no need to pay money, or share your bank card details. See details in the comments."
  )
openai.api_key = os.getenv('OPENAI_API_KEY')

###############################################################################
# technical part - we call ChatGTP and print its response.
###############################################################################
for prompt in prompts:
  sleep_if_needed()
  long_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": 'user',
      "content": prompt
    }],
    temperature=temperature  # a number between 0 and 1
    # temperature is the degree of randomness of the model's output
  )
  add_now()
  print(f""""

Your query: `{prompt}`
  
ChatGPT run with temperature {temperature} has generated {len(long_response.choices)} response(s):
""")
  for i, choice in enumerate(long_response.choices):
    response = choice.message["content"]
    print(f"Response #{i}: `{response}`\n\n" )
