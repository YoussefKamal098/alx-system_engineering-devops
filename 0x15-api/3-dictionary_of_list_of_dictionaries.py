#!/usr/bin/python3
"""
This script retrieves and exports the tasks of all users from a fake
online REST API service (https://jsonplaceholder.typicode.com) to a JSON file.

Usage:
    python script_name.py

Description:
    - It fetches the user details from the JSONPlaceholder API.
    - It fetches the list of tasks from the same API.
    - It writes the tasks of users to a JSON file.

Example:
    python script_name.py

The generated JSON file will be named "todo_all_employees.json".
"""
from datetime import datetime
import json
import requests
import sys


def fetch_data(url):
    """
    Fetch data from the given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: The JSON response from the URL.

    Raises:
        SystemExit: If there is an error fetching data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching data from {url}: {err}")
        sys.exit(1)


def get_user_tasks(user_id):
    """
    Get tasks for the specified user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of tasks for the specified user.
    """
    # Fetch the user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user = fetch_data(user_url)

    # Check if the user exists
    if not user:
        print(f"No user found with ID {user_id}.")
        sys.exit(1)

    # Fetch the tasks data
    tasks_url = 'https://jsonplaceholder.typicode.com/todos/'
    tasks = fetch_data(tasks_url)

    # Filter tasks to get only those belonging to the specified user
    return list(filter(lambda task: task.get('userId') == user_id, tasks))


def fetch_and_format_user_tasks(user_id):
    """
    Fetch and format tasks for the specified user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of formatted tasks for the specified user.
    """
    # Fetch the user data
    user = fetch_data(f'https://jsonplaceholder.typicode.com/users/{user_id}')

    # Check if the user exists
    if not user:
        print(f"No user found with ID {user_id}.")
        sys.exit(1)

    # Get user tasks
    user_tasks = get_user_tasks(user_id)

    # Format the tasks for the user
    tasks = [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in user_tasks]

    return tasks


def export_to_json(
        filename=f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}users_tasks'
):
    """
    Export tasks for all users to a JSON file.

    Args:
        filename (str): The name of the JSON file.
    """
    # Fetch the list of users
    users = fetch_data('https://jsonplaceholder.typicode.com/users')

    # Check if any users were found
    if not users:
        print("No users found.")
        sys.exit(1)

    # Create a dictionary to store tasks for all users
    all_tasks = {}

    # Loop through each user and get their tasks
    for user in users:
        user_id = user.get('id')
        all_tasks[str(user_id)] = fetch_and_format_user_tasks(user_id)

    # Write the tasks to a JSON file
    with open(f'{filename}.json', 'w') as file:
        json.dump(all_tasks, file)

    print(f"Tasks have been exported to {filename}.json")


def main():
    """
    The main function that drives the script.
    """
    # Export tasks to JSON file
    export_to_json("todo_all_employees")


if __name__ == "__main__":
    main()
