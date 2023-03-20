import sys
from chatgpt import ChatGPT

qa = ChatGPT(max_histories=3, memory_ttl=15, db_name='./.qa_histories')

reply = qa.qa(sys.argv[1])
print(reply)
