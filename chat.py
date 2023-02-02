import os
import openai
import time

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

text_input = str(input('Enter your text: '))
text_input = text_input.strip()

start = time.time()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Human:"+ text_input +"\n "+" AI:\n",
  temperature=0.7,
  max_tokens=3000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print("\n\n"+response["choices"][0]["text"]+"\n\n")
length = len(response["choices"][0]["text"])
elapsed = round((time.time() - start), 2)
print("elapsed: " , elapsed , "s", "length: ", length, "speed: ", round(length/elapsed), "char/s")
print("finish reason: ", response["choices"][0]["finish_reason"])
