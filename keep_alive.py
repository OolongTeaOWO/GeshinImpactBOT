from flask import render_template,redirect
from threading import Thread
from flask import Flask
import requests
import logging
import random
import time

app = Flask('')
@app.route('/')
def home():
    return ("好欸")

#設定網站簡易頁面

def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000)) 
def ping(target, debug):
    while(True):
        r = requests.get(target)
        if(debug == True):
            print(f"\033[1;90m * Status code：{r.status_code}\033[0m")
        time.sleep(random.randint(30,60)) #alternate ping time between 3 and 5 minutes
def awake(target, debug=False):  
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True  
    t = Thread(target=run)
    r = Thread(target=ping, args=(target,debug,))
    t.start()
    r.start()
