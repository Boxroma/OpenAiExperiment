import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# save prompt from terminal 
prompt = sys.argv

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

count = 1
for object in response.choices:
    print("Response: " + str(count))
    print(object.text + "\n")
    count += 1