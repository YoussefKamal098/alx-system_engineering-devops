#!/usr/bin/python3
"""
This script retrieves and exports the tasks of a specified user from a fake
online REST API service (https://jsonplaceholder.typicode.com) to a JSON file.

Usage:
    python script_name.py <user_id>

Where <user_id> is the ID of the user whose tasks you want to export.

Description:
    - The script takes one command-line argument: the user ID.
    - It fetches the user details from the JSONPlaceholder API.
    - It fetches the list of tasks from the same API.
    - It filters the tasks to get only those belonging
        to the specified user.
    - It writes the user's tasks to a JSON file.

Example:
    python script_name.py 1

The generated JSON file will be named with the current date and time.
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

    # Filter tasks to get only those belonging to
    # the specified user and return them
    return list(filter(lambda task: task.get('userId') == user_id, tasks))


def export_to_json(
        user_id,
        filename=f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}user_tasks'
):
    """
    Export tasks for the specified user to a JSON file.

    Args:
        user_id (int): The ID of the user.
        filename (str): The name of the
            CSV file (default: current date and time).
    """
    # Fetch the user data
    user = fetch_data(f'https://jsonplaceholder.typicode.com/users/{user_id}')

    # Check if the user exists
    if not user:
        print(f"No user found with ID {user_id}.")
        sys.exit(1)

    # Get user tasks
    user_tasks = get_user_tasks(user_id)

    # Write the tasks to a CSV file
    with open(f"{filename}.json", "w") as file:
        tasks = [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in user_tasks]

        json.dump({str(user_id): tasks}, file)

    print(f"Tasks have been exported to {filename}.json")


def main():
    """
    The main function that drives the script.
    """
    # Ensure the script receives the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    try:
        userId = int(sys.argv[1])
    except ValueError:
        print("Error: <user_id> must be an integer.")
        sys.exit(1)

    # Export tasks to JSON file
    export_to_json(userId, str(userId))


if __name__ == "__main__":
    main()
