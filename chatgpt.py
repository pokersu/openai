import openai
import backoff
import pickle
import os
import time


class ChatGPT:
    max_histories: int
    memory_ttl: int
    histories: list
    model_name: str
    db_name: str


    def __init__(self, model_name='gpt-3.5-turbo', max_histories=15, memory_ttl=20*60, db_name='./.histories') -> None:
        self.max_histories = max_histories
        self.memory_ttl = memory_ttl
        self.model_name = model_name
        self.db_name = db_name
        if os.path.exists(self.db_name):
            self.histories=pickle.load(open(self.db_name, 'rb'))
        else:
            self.histories = []

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def completions_with_backoff(self, **kwargs):
        return openai.ChatCompletion.create(**kwargs)


    def _get_messages(self, role, content):

        while len(self.histories)>self.max_histories:
            self.histories.pop(0)
        
        first_timestamp = self.histories[0]['timestamp'] if len(self.histories)>0 else int(time.time())
        last_timestamp = self.histories[-1]['timestamp'] if len(self.histories)>0 else int(time.time())

        if int(time.time()-last_timestamp)>self.memory_ttl:
            self.histories = []
        self.histories.append({'timestamp':int(time.time()), 'role':role,'content': content})
        if first_timestamp!=0:
            self.histories.insert(0, {'timestamp':0, 'role':'system','content':'You are a helpful assistant'})
        pickle.dump(self.histories, open(self.db_name, 'wb'))
        messages = map(lambda x: {'role': x['role'], 'content': x['content']}, self.histories)
        return list(messages)

    def ask(self, question):
        messages = self._get_messages('user', question)
        response = self.completions_with_backoff(model=self.model_name, messages=messages)
        output_text = response['choices'][0]['message']['content']
        self._get_messages('assistant', output_text)
        return output_text

    def qa(self, question):
        response = self.completions_with_backoff(model=self.model_name, messages=[{'role': 'user', 'content': question}])
        return response['choices'][0]['message']['content']
        

