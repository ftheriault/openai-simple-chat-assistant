# Simple Chat bot and assistant tests using OpenAI

This is my first attempt to build a ChatBot using the OpenAI API.

## Getting started

1. Install openai : `pip install openai`
2. Retrieve your OPENAI API key (https://platform.openai.com)
3. Create a `.env` file, and put your key in it, for example :

```
OPENAI_API_KEY=sk-xxxx-ty234dsf6w2343twerfasdff
```

4. Run `chat-completion.py`

## Documentation

### AI types

There seems to be two types of APIs:

- Chat completion : Simpler to use
- Assistant API : More complex, requires configuration and more API calls. Better for long conversations and for adding proprietary knowledge/documents/data with RAG (Retrieval-Augmented Generation).

Sources:
- https://medium.com/leniolabs/exploring-openais-apis-assistants-vs-chat-completions-91525f73422c
- https://platform.openai.com/docs/assistants/tools/knowledge-retrieval

### Creating messages

#### Message roles

When creating a message in the conversation, it can have one of 3 roles :
- user : A message written by the user, which is sent to the assistant
- system : Context given to the ChatBot in order to customize it.
- assistant : Response from the ChatBot. By keeping messages, it allows a continuous conversation with history
- tool : I have not found information on this role, yet.

#### Examples of system messages

The following system messages completely changes how the assistant answers :
- "Translate the exact message written by the user in Spanish"
- "All answers must be exactly 15 words long"
- "You are an emotional assistant"