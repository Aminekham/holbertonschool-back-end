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
        if i['id'] == int(argv[1]):
            emp = i['username']
    for i in resp_todos.json():
        if i['userId'] == int(argv[1]):
            small_dic = {}
            small_dic["task"] = i['title']
            small_dic["completed"] = i['completed']
            small_dic["username"] = emp
            json_list.append(small_dic)
    json_dic[argv[1]] = json_list
    with open(f"{argv[1]}.json", 'w') as f:
        json.dump(json_dic, f)
