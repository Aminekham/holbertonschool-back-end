#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import requests 
import json
from sys import argv


resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
resp_users = requests.get('https://jsonplaceholder.typicode.com/users')

t, d = 0, 0
for i in resp_todos.json():
    if i['userId'] == int(argv[1]):
        t = t + 1
        if i['completed'] == True:
            d = d + 1
for i in resp_users.json():
    if i['id'] == int(argv[1]):
        emp = i['name']

print(f"Employee {emp} is done with tasks({d}/{t})")

for i in resp_todos.json():
    if i['userId'] == int(argv[1]):
        print(f"  {i['title']}")
