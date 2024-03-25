#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a given employee ID using a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee whose progress is to be retrieved.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)
        employee_name = todos[0]['username']

        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

