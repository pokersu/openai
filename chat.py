import sys
import openai
import os
from chatgpt import ChatGPT

openai.api_key=os.getenv('OPENAI_KEY')

chat = ChatGPT(db_name='./.chat_histories')

reply = chat.ask(sys.argv[1])
print(reply)
