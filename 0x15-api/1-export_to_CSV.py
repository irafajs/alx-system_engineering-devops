#!/usr/bin/python3
"""
Shebang to make a py script
"""


import csv
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
        csv_filename = f'{u_d["id"]}.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for task in todos:
                csv_writer.writerow([u_d["id"], u_d["username"], str(
                    task["completed"]), task["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    get_employee_todo_progress(sys.argv[1])
