from langchain_community.document_loaders import DirectoryLoader,TextLoader,PyPDFLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings)
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore

openai_api_key=''
index_name = ''
pinecone_api_key=''
embeddings= OpenAIEmbeddings(api_key=openai_api_key)
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

# load/read the document
directory= "knowledge_base/"
loader = DirectoryLoader(directory,glob="*.txt", loader_cls=TextLoader)
loaded_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=10)
print("Document has been loaded.")

# split it into chunks
print("Splitting documents")
splitted_docs = text_splitter.split_documents(loaded_documents)
print("Document splitted,Generating embeddings..")

#load into pinecone
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings,pinecone_api_key=pinecone_api_key)

#FOR DELETION OF PINECONE INDEXES
#vectorstore.delete(delete_all=True)
#print("All embeddings deleted from vectorstore...")

vectorstore.add_documents(splitted_docs)
print("Embeddings generated and loaded into vectorstore...")

