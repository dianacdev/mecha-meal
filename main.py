from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic 

#LOAD .ENV
load_dotenv()

#SETUP LLM
llm = ChatOpenAI(model="gpt-4")

#llm = ChatAnthropic() if you do anthropic claude etc.
