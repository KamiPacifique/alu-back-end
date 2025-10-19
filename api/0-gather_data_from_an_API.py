#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress
using a REST API, based on the employee ID provided.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL
    url = "https://jsonplaceholder.typicode.com"

    # Get user data
    user_response = requests.get(f"{url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODOs for the user
    todos_response = requests.get(f"{url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    num_done = len(done_tasks)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
