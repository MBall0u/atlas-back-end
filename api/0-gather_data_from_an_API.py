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
    except VslueError:
        print("invalid employee id provided")
        return

    employee_get = requests.get(
        "https//jsonplaceholder.typicode.com/user/{}".format(employee_id))
    tasks_get = requests.get(
        "https//jsonplaceholder.typicode.com/todos")

    if employee_get.status_code != 200 or tasks_get.status_code != 200:
        print("one or more GET requests have failed")
        return

    employee_json = employee_get.json()
    tasks_json = tasks_get.json()

    employee_name = employee_json['name']
    employee_tasks = [
        task for task in tasks_json if task['userId'] == employee_id]

    total_tasks = len(employee_tasks)
    completed_tasks = len(
        [task for task in employee_tasks if task['completed']])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        completed_tasks,
        total_tasks))

    for task in employee_tasks:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    request_processor()
