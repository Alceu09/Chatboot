from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain.vectorstores import FAISS  
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def create_vectorstore(chunks):
    api= ''

    embeddings=OpenAIEmbeddings(openai_api_key=api)   # Carregando os embeedings da open ai,   #
    
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings) # criando a vector store com nossos textos  #
    
    return vectorstore

def create_conversaçao_chain (vectorstore):  # Vai fazer ranqueamento do prompt #
    api= ''
    
    
    llm=ChatOpenAI(openai_api_key=api)
    
    memory=ConversationBufferMemory(memory_key='chat_history', return_messages=True)  # Criando a memoria da conversaçao , historico da conversa do user#
    
    consersation_chain=ConversationalRetrievalChain.from_llm (llm=llm,retriever=vectorstore.as_retriever(), memory=memory)  # Criando a conversaçao com o retriever e a memoria , retriver vai buscar dentro da corrente de consersa e olhar o que é similar  #
    return consersation_chain
    
    