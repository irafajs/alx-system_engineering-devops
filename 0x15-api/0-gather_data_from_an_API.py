#!/usr/bin/python3
"""
Shebang to make a py script
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """fetch employess to do list using his identifincation"""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    response = requests.get(url)

    if response.status_code == 200 and user_response.status_code == 200:
        u_d = user_response.json()
        todos = response.json()
        completed_tasks = [task for task in todos if task['completed']]
        n_c_t = len(completed_tasks)
        t_n_t = len(todos)
        print(f"Employee {u_d['name']} is done with tasks({n_c_t}/{t_n_t}): ")
        for task in completed_tasks:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    get_employee_todo_progress(sys.argv[1])
