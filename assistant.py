import os
from openai import OpenAI

# This is a simple example of how to use the OpenAI API to create an assistant and ask it a question.
# It will upload a file to the API, create an assistant, ask a question, and then delete the assistant and the file.

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

file = client.files.create(
  file=open("data/invoices.pdf", "rb"),
  purpose='assistants'
)

# If you need to create a new assistant (they are permanent)
assistant = client.beta.assistants.create(
    instructions="You are an invoicing assistant, giving insights based on previous invoices.",
    name="Invoice Assistant",
    tools=[{"type": "retrieval"}],      # tools=[{"type": "code_interpreter"}]
    model="gpt-4-turbo",
    file_ids=[file.id]
)

question = input("Your question about your invoices (leave empty to quit) : ")

if not question:
    exit()

# If you need to fetch an assistant by ID instead of creating one
assistantId = assistant.id # os.environ.get("ASSISTANT_ID")
assistant = client.beta.assistants.retrieve(assistantId)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=question
)

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Try to aggregate as much as possible.",
)

if run.status == 'completed':
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages.data[0].content[0].text.value)
else:
  print(run.status)

# Detach the uploaded file from the assistant (optional)
client.beta.assistants.files.delete(
  assistant_id=assistant.id,
  file_id=file.id
)

# Delete the uploaded file (optional)
client.files.delete(file.id)

# Delete thread/conversation
response = client.beta.threads.delete(thread.id)

# Delete assistant
response = client.beta.assistants.delete(assistant.id)