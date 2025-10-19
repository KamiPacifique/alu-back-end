#!/usr/bin/python3
"""Exports employee TODO list to CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_info = user_response.json()
    todos_info = todos_response.json()

    username = user_info.get("username")

    csv_file = f"{employee_id}.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_info:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
