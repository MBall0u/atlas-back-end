#!/usr/bin/python3
"""
This script gets information from a rest API and then sorts
through it and prints a formatted string
"""

import requests
import sys


def request_processor():
    """
    returns information about an employees todo list progress
    """
    if len(argv) < 2:
        print("no employee id provided")
        return

    employee_id = argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("invalid employee id provided")
        return

    employee_url = "https//jsonplaceholder.typicode.com/user/{}".format(
        employee_id)
    tasks_url = "https//jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)

    employee_get = requests.get(employee_url)
    tasks_get = requests.get(tasks_url)

    if employee_get.status_code != 200:
        print("employee not found")
        return

    tasks_json = tasks_get.json()

    employee_name = employee_get.json().get("name")

    total_tasks = len(tasks_json)
    completed_tasks = [task for task in tasks_json if task.get("completed")]
    total_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        completed_tasks,
        total_tasks))

    for task in employee_tasks:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    request_processor()
