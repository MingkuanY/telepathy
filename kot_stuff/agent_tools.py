from langchain.agents import Tool
import pandas as pd
import os
import sys

from langchain_nvidia_ai_endpoints import ChatNVIDIA

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory

from langchain_community.document_loaders import TextLoader


import nemo_retriever_client as nrc 



#each retriever client has its own vector store
def make_mingkuan_retriever_client():
    global retriever_client_mingkuan_collection
    
    base_directory = "./rag_info/"
    retriever_client_general_collection = nrc.RetrieverClient()
    loader = TextLoader(base_directory+"mingkuan.txt")
    document = loader.load()
    retriever_client_general_collection.add_files(document)



def set_llm_client(client):
    global llm_client
    llm_client = client

def deploy_tools(query, LANGCHAIN_KEY):

    llm = ChatNVIDIA(
        model="meta/llama-3.1-405b-instruct",
        api_key=LANGCHAIN_KEY
    )

    tools=[mingkuan_tool]

    memory = ConversationBufferMemory()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        memory=memory
    )

    my_full_prompt = "Answer the following question(s): " + query
    return agent.invoke({"input": my_full_prompt})



# RAG search in User Directory collection (tool 1)
def mingkuan_search(query):
    #Send user query to Retriever for RAG

    raw_prompt = "Use the given context to extract information relevant to this parameter. \n\nParameter: "
    return retriever_client_mingkuan_collection.rag_query(query, raw_prompt)


mingkuan_search_tool = Tool(
    name="search_user_directory",
    func=mingkuan_search,
    description="User Directory: database about the person Ming Quan"
)