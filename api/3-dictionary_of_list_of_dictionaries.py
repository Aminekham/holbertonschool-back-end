#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import json
import requests


if __name__ == '__main__':

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    mo = 'https://jsonplaceholder.typicode.com/todos?userId='
    employee = response.json()
    di = {}
    for a in employee:
        id = a['id']
        todos = requests.get(
            mo + str(id)).json()
        b = []
        for s in todos:
            lis1 = {}
            lis1["username"] = a["username"]
            lis1["task"] = s['title']
            lis1["completed"] = s['completed']
            b.append(lis1)
        di[id] = b
    with open('todo_all_employees.json', 'w') as file:
        json.dump(di, file)
