import requests
import json

url = f"http://192.168.101.254/api/v1/ticket"

payload = {
    "username": "admin",
    "password": "admin123"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    ticket = response.json()["response"]["serviceTicket"]
    print("Service Ticket:", ticket)
else:
    print("Hiba történt:", response.status_code, response.text)

###################################################

import requests


ticket = input("Add meg a service ticket-et: ")

url = f"http://192.168.101.254/api/v1/network-device"

headers = {
    "X-Auth-Token": ticket
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()["response"]

    for dev in devices:
        platform = dev.get("platformId", "N/A")
        ip = dev.get("managementIpAddress", "N/A")
        print(f"Platform ID: {platform}, Management IP: {ip}")

else:
    print("Hiba történt:", response.status_code, response.text)
