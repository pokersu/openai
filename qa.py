import sys
import openai
import os
from chatgpt import ChatGPT

openai.api_key=os.getenv('OPENAI_KEY')

qa = ChatGPT(max_histories=3, memory_ttl=15, db_name='./.qa_histories')

reply = qa.qa(sys.argv[1])
print(reply)
