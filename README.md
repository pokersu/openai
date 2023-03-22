# chatgpt command line tool

a chatgpt tool based on command tool. It can avoid the need to frequently switch proxy software in use. 
and you can based on this tool build other application, just need call this shell script and handle the result in your application.

and even you can use it in you iphone shortcut command, in your shortcut command app call your server ssh. and use shortcut command by siri


or you can use it do anything in linux shell, maybe you can use it extract some keyword from a text and pipe it to another ai application, such as stable diffusion to generate a image

### requirement

1. install proxychains 

*you need prepare a proxy that openai usable. (non hk, china)* 

proxychains config:

**debian install** 
```bash
sudo apt install proxychains4
```
**proxychains config** 

*change last line sock5 proxy to your proxy local port* 
```
....
socks5  127.0.0.1 1080
```


2. clone repo

```
git clone https://github.com/pokersu/openai.git
```


3. config tools

**openai key and workdir** 

*your profile config: /etc/profile or $home/.bashrc* 

```
export OPENAI_WORKDIR=your repo location
export OPENAI_KEY=your openai key
```


### usage

1. chat normal

```
chatgpt question?
```

2. chat brief result

```
chatgpt -b question?
```


3. qa

```
chatgpt -q context question
```



### about


- brief chat you can use it in vim or other editor, when you ask gpt generate some code. the result will more clearly
- chat mode will has some memory for history, 15 times chat and less than 20min, if over this limit, the memory will loss
- qa mode need you prepare input context and the question for this context , and important : no memory 
- default use chatgpt 3.5 turbo model, if you want change that , please change it in chatgpt.py
