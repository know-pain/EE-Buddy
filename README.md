
---

# About EE Buddy

This repository contains code and guidelines on how to set up EE Buddy while demonstrating the capabilities of RAG AI Chatbots in universities or institutions of learning. This chatbot uses the power of OpenAI's GPT-3.5 model, Langchain, Chainlit, and Pinecone to create an AI solution that can provide informative responses to users' queries using a knowledge base through a simple yet effective user interface.

## Getting Started

To get started with the demo, you will need to have Python (3.8 or above) installed on your machine. You will also need to install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
```

Then, follow these steps to set up your environment variables:

1. Create a `.env` file in the root directory of your project.
2. Copy the contents of the `api.txt` file into the `.env` file.
3. Fill in your API keys as necessary.

For more detailed guidelines on how to get the API keys:

- CHAINLIT_AUTH_SECRET: [here](https://docs.chainlit.io/authentication/overview)
- OPENAI_API_KEY: [here](https://platform.openai.com/account/api-keys)
- OAUTH_GOOGLE_CLIENT_ID: [here](https://docs.chainlit.io/authentication/oauth)
- OAUTH_GOOGLE_CLIENT_SECRET: [here](https://docs.chainlit.io/authentication/oauth)
- PINECONE_API_KEY: [here](https://docs.pinecone.io/guides/get-started/quickstart)
- LITERAL_API_KEY: [here](https://docs.getliteral.ai/get-started/installation)

Additionally, insert the API keys in `db_insert.py`. This script is for populating the vector database with custom knowledge to be used by the chatbot. To run the script:

1. Open `db_insert.py` in VS Code.
2. Click the dropdown menu near the run code button.
3. Select "Run Python File."

Only text files are enabled to be populated. Save the text files in the `knowledge_base` folder before running `db_insert`.

The `db_insert` script doesn't support upserting, so if one document is used more than once, it will create duplicates. I'm sure there's a way to fix this but I'm fairly new to programming and couldn't figure it out :-).

## Usage

After populating the vector database with at least two documents, start the chatbot by running the following command in the terminal in VS Code:

```bash
chainlit run app.py
```

For more details, check out Chainlit's official documentation [here](https://docs.chainlit.io/get-started/overview).

To end the chatbot, close the Chainlit terminal in VS Code or press `Ctrl+C` in VS Code to stop the local server from running.

## EE Buddy

This is a simple chatbot that uses OpenAI's GPT-3.5-turbo language model to generate responses to user input, Langchain as a chaining agent/framework, Pinecone as a vector database using OpenAI embedding models to generate the vector embeddings, and Chainlit for its user interface.
This chatbot was made as a school project to serve as an assistant for students and staffs,providing accurate and timely responses day in,day out without downtimes.Although its far from perfect(due to my very limited expertise in programming),it could become much much more powerful in the right hands.Have fun exploring its capabilities!!

## Acknowledgments

- [Langchain](https://www.langchain.com/)
- [Chainlit](https://chainlit.io/)
- [OpenAI](https://openai.com/)
- [Pinecone](https://www.pinecone.io/)

---
