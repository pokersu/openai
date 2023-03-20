import sys
from chatgpt import ChatGPT

chat = ChatGPT(db_name='./.chat_histories')

reply = chat.ask(sys.argv[1])
print(reply)
