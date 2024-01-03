#!/usr/bin/python3
"""
Shebang to create a py script
"""


import json
import requests
import sys


def get_all_employees_todo():
    """Fetch tasks for all employees"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    todos_response = requests.get(url)

    if users_response.status_code == 200 and todos_response.status_code == 200:
        users_data = users_response.json()
        todos = todos_response.json()

        all_employees_tasks = {}

        for user_data in users_data:
            user_id = user_data['id']
            user_tasks = [
                {
                    "username": user_data['username'],
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in todos if task['userId'] == user_id
            ]

            all_employees_tasks[user_id] = user_tasks

        json_filename = 'todo_all_employees.json'
        with open(json_filename, 'w') as json_file:
            json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    get_all_employees_todo()
