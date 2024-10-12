# pip install --upgrade --quiet gigachain==0.2.6 gigachain_community==0.2.6 gigachain-cli==0.0.25 duckduckgo-search==6.2.4 pyfiglet==1.0.2 langchain-anthropic llama_index==0.9.40 pypdf==4.0.1 sentence_transformers==2.3.1

from langchain.chat_models.gigachat import GigaChat

from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate
)

from typing import List, Optional, Union

from langchain.tools import tool

from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext

import getpass
import requests
import uuid


# # 1. GigaChat
# Define GigaChat throw langchain.chat_models
def get_giga(giga_key: str) -> GigaChat:
    chat = GigaChat(verify_ssl_certs=False, credentials=giga_key, model="GigaChat")
    return chat

def test_giga():
    giga_key = getpass.getpass("Enter your GigaChat credentials: ")
    giga = get_giga(giga_key)


# # 2. Prompting
# ### 2.1 Define classic prompt

# Implement a function to build a classic prompt (with System and User parts)
def get_prompt(user_content: str) -> List[Union[SystemMessage, HumanMessage]]:
    system_message = SystemMessage(content="Act as Machine Learning Engineer.")
    human_message = HumanMessage(content=user_content)
    return [system_message, human_message]

# Let's check how it works
def test_prompt():
    giga_key = getpass.getpass("Enter your GigaChat credentials: ")
    giga = get_giga(giga_key)
    user_content = 'Hello!'
    prompt = get_prompt(user_content)
    res = giga(prompt)
    print (res.content)

# ### 3. Define few-shot prompting

# Implement a function to build a few-shot prompt to count even digits in the given number. The answer should be in the format 'Answer: The number {number} consist of {text} even digits.', for example 'Answer: The number 11223344 consist of four even digits.'
def get_prompt_few_shot(number: str) -> List[HumanMessage]:
    system_message = SystemMessage(content="You are a helpful assistant. Your task is to count the number of even digits in a given number and format the response as 'Answer: The number {number} consist of {n} even digits.'")
    examples = [
        HumanMessage(content="Answer: The number 11223344 consist of four even digits."),
        HumanMessage(content="Answer: The number 2468 consist of four even digits."),
        HumanMessage(content="Answer: The number 1234 consist of two even digits."),
    ]
    task_prompt = HumanMessage(content=f"Answer: The number {number} consist of how many even digits?")
    return [system_message] + examples + [task_prompt]

# Let's check how it works
def test_few_shot():
    giga_key = getpass.getpass("Enter your GigaChat credentials: ")
    giga = get_giga(giga_key)
    number = '62388712774'
    prompt = get_prompt_few_shot(number)
    res = giga.invoke(prompt)
    print (res.content)

# # 4. Llama_index
# Implement your own class to use llama_index. You need to implement some code to build llama_index across your own documents. For this task you should use GigaChat Pro.
class LlamaIndex:
    def __init__(self, path_to_data: str, llm: GigaChat):
        self.llm = llm
        self.system_prompt="""
        You are a Q&A assistant. Your goal is to answer questions as
        accurately as possible based on the instructions and context provided.
        """
        documents = SimpleDirectoryReader(path_to_data).load_data()
        hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        langchain_embedding = LangchainEmbedding(hf_embeddings)
        self.service_context = ServiceContext.from_defaults(embed_model=langchain_embedding, chunk_size=1024, llm=self.llm)
        self.index = VectorStoreIndex.from_documents(documents, service_context=self.service_context)

    def query(self, user_prompt: str) -> str:
        query_engine=self.index.as_query_engine()
        user_input = self.system_prompt + user_prompt
        query_response = query_engine.query(user_input)
        return query_response.response



# Let's check
def test_llama_index():
    giga_key = getpass.getpass("Enter your GigaChat credentials: ")
    giga_pro = GigaChat(credentials=giga_key, model="GigaChat-Pro", timeout=30, verify_ssl_certs=False)

    llama_index = LlamaIndex("data/llm/docs_for_llama_index", giga_pro)
    res = llama_index.query('what is attention is all you need?')
    print (res)
