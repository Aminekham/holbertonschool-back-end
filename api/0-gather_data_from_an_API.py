#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
Requirements:
You must use urllib or requests module
The script must accept an integer as a parameter, which is
the employee ID
The script must display on the standard output the employee TODO
list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
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
