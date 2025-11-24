import requests
import json

CONTROLLER = "http://192.168.101.254"
USERNAME = "admin"
PASSWORD = "admin123"

url = f"{CONTROLLER}/api/v1/ticket"

payload = {
    "username": USERNAME,
    "password": PASSWORD
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    ticket = response.json()["response"]["serviceTicket"]
    print("Service Ticket:", ticket)
else:
    print("Hiba a ticket lekérésekor:", response.text)
