import requests
from time import sleep

u = "https://ch462601334.challenges.eng.run/"
for i in range(10):  
    r = requests.get(u)
    if r.status_code == 200:
        print(f"{r.text}")
    sleep(20)