import streamlit as st
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chromaRdr2"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    # formatted_response = f"Response: {response_text}\nSources: {sources} \n Context: {context_text}"
    formatted_response = f"Response: {response_text}"
    return formatted_response

# Streamlit app
st.title('Osimosi LLM :) ')

# Initialize session state for messages if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Loop through the messages in the session state and display them
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build a prompt input template for the user
prompt = st.chat_input("Enter your prompt here")

# When user presses enter, run the following code
if prompt:
    st.chat_message('user').markdown(prompt)

    # Store the prompt in the session state
    st.session_state.messages.append({'role': 'user','content': prompt})

    # Use st.spinner to show a loading animation while querying the database
    with st.spinner('Loading...'):
        # Query the database and get the response
        response = query_rag(prompt)

    # Display the response in the Streamlit chat interface
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({'role': 'assistant','content': response})