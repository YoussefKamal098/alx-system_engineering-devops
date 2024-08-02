#!/usr/bin/python3
"""
This script retrieves and displays the completion status of
tasks for a specified user from a fake online REST API
service (https://jsonplaceholder.typicode.com).

Usage:
    python script_name.py <user_id>

Where <user_id> is the ID of the user whose tasks you want to retrieve.

Description:
    - The script takes one command-line argument: the user ID.
    - It fetches the user details from the JSONPlaceholder API.
    - It fetches the list of tasks from the same API.
    - It filters the tasks to get only those belonging to the specified user.
    - It further filters the tasks to get only those that are completed.
    - It prints the user's name and the number of completed tasks out
        of the total tasks.
    - It lists the titles of the completed tasks.

Example:
    python script_name.py 1
"""
import sys
import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)


def main():
    # Ensure the script receives the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    try:
        userId = int(sys.argv[1])
    except ValueError:
        print("Error: <user_id> must be an integer.")
        sys.exit(1)

    # Fetch the user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{userId}'
    user = fetch_data(user_url)

    # Check if the user exists
    if not user:
        print(f"No user found with ID {userId}.")
        sys.exit(1)

    # Fetch the tasks data
    tasks_url = 'https://jsonplaceholder.typicode.com/todos/'
    tasks = fetch_data(tasks_url)

    # Filter tasks to get only those belonging to the specified user
    user_tasks = list(filter(lambda task: task.get('userId') == userId, tasks))

    # Filter tasks to get only those that are completed
    user_completed_tasks = list(
        filter(lambda task: task.get('completed'), user_tasks)
    )

    # Print the completion status
    print(f"Employee {user.get('name')} is done with tasks("
          f"{len(user_completed_tasks)}/{len(user_tasks)}):")

    # Print the titles of the completed tasks
    for task in user_completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
