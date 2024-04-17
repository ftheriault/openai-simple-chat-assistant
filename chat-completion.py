import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Message history for the conversation
messages = [
    {"role": "system", "content": "Each response must be answered in less than 15 words."},
]

MAX_TOKENS = 150            # Each word is approximately 1.2 tokens (1M tokens = 10$ approx.)
MODEL="gpt-4-turbo"         # The model to use for the conversation
message = "<will change>"

while True:
    message = input("Your message (leave empty to quit) : ")

    if not message:
        break

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        max_tokens=MAX_TOKENS,
    )

    if response.choices and len(response.choices) > 0:
        response = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        print("Assistant : ", response)
    else:
        print("No response from the assistant. Please try again.")
