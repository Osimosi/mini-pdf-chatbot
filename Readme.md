# Project Report: Implementing RAG with Pretrained LLM for Red Dead Redemption 2 Game Guidebooks

## Introduction
The aim of this project is to implement the Retrieval-Augmented Generation (RAG) technique with a pretrained language model (LLM) for creating a mini chatbot focused on providing information from PDF guides related to the video game "Red Dead Redemption 2" (RDR2). This report outlines the methodology, implementation details, and outcomes of the project.

## Background
"Red Dead Redemption 2" is a popular open-world action-adventure game developed by Rockstar Games. It offers an expansive game world with various missions, activities, and challenges. As players navigate through the game, they often seek guidance and information from online guides and resources. This project aims to leverage these guides stored as PDF documents to provide relevant assistance through a chatbot interface.

## Methodology
### Data Collection
PDF guides related to "Red Dead Redemption 2" were collected and stored in a designated data directory.

### Preprocessing
The PDF documents were processed using the LangChain library to extract text content. The documents were split into smaller chunks for efficient storage and retrieval.

### Embedding Generation
The Ollama embeddings, specifically the llama3 model, were used to generate embeddings for each text chunk. These embeddings capture semantic information essential for similarity-based retrieval.

### Database Population
A Chroma vector store was utilized to store the text chunks along with their corresponding embeddings. This facilitated efficient retrieval of relevant information based on user queries.

### RAG Implementation
The RAG technique was implemented using the Ollama library. User queries were used to retrieve relevant context from the database, which was then utilized to generate responses using the pretrained LLM (llama3).

## Implementation Details
### Code Structure
- **get_embeddings_function.py**: Defines a function to obtain the embedding model.
- **populate_database.py**: Populates the Chroma database with text chunks and their embeddings extracted from PDF guides.
- **query_db_streamlit.py**: Implements the Streamlit interface for user interaction and integrates the RAG model to provide responses based on user queries.

## Results
The implemented chatbot successfully provides responses based on user queries related to "Red Dead Redemption 2". This can be verified by using the different numerical test cases provided in the directory in the form of images from the original guide. Users can interact with the chatbot through a user-friendly Streamlit interface, receiving relevant information extracted from the provided PDF guides.

## Future Enhancements
- Integration of additional PDF guides to expand the knowledge base.
- Fine-tuning the pretrained LLM model for better contextual understanding and response generation.
- Enhancing the user interface with features such as multimedia support and natural language understanding.

## Conclusion
This project demonstrates the effective implementation of the RAG technique with a pretrained language model for creating a chatbot focused on "Red Dead Redemption 2" guides. By leveraging the Ollama embeddings and Chroma vector store, the chatbot efficiently retrieves and generates responses, enhancing the user experience and providing valuable assistance to players seeking information about the game.