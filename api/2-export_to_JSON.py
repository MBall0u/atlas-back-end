#!/usr/bin/python3
"""
This script gets information from a rest API and then sorts
through it and prints a formatted string
"""

import csv
import json
import requests
import sys


def request_processor():
    """
    returns information about an employees todo list progress
    """
    if len(sys.argv) < 2:
        print("no employee id provided")
        return

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("invalid employee id provided")
        return

    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)

    employee_get = requests.get(employee_url)
    tasks_get = requests.get(tasks_url)

    if employee_get.status_code != 200:
        print("employee not found")
        return

    tasks_json = tasks_get.json()

    employee_name = employee_get.json().get("username")

    total_tasks = len(tasks_json)
    completed_tasks = [task for task in tasks_json if task.get("completed")]
    total_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        total_completed_tasks,
        total_tasks))

    task_list = []
    for task in tasks_json:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        task_list.append(task_data)
    json_data = {employee_id: task_list}

    json_file_name = "{}.json".format(employee_id)
    with open(json_file_name, 'w', newline='') as jsonfile:
        json.dump(json_data, jsonfile, seperators=(",", ":"))
    return json_data


if __name__ == "__main__":
    request_processor()
