#!/usr/bin/python3
"""
Shebang to make a py script
"""


import requests
import json
import sys


def get_employee_todo_progress(employee_id):
    """Fetch tasks for a specific employee"""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos = todos_response.json()

        employee_tasks = [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            for task in todos
        ]

        json_filename = f'{employee_id}.json'
        with open(json_filename, 'w') as json_file:
            json.dump({employee_id: employee_tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
