#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json_dic = dict()
    json_list = list()
    small_dic = dict()
    for i in resp_users.json():
        for j in resp_todos.json():
            small_dic = {}
            small_dic["task"] = j['title']
            small_dic["completed"] = j['completed']
            small_dic["username"] = i['username']
            json_list.append(small_dic)
        json_dic[i['id']] = json_list
        with open("todo_all_employees.json", 'w') as f:
            json.dump(json_dic, f)
