import json


def calculate_progress(completed, total):
    progress = (completed / total) * 100
    return progress


def get_status(completed, total):

    if completed == total:
        return "All applications completed"

    else:
        return "Work still remaining"

def get_positive_number(message):

    while True:

        try:
            number = int(input(message))

            if number <= 0:
                print("Please enter a positive number.")
                continue

            return number

        except ValueError:
            print("Please enter a valid number.")

def get_completed_number(message, total_applications):

    while True:

        try:
            number = int(input(message))

            if number < 0:
                print("Completed applications cannot be negative.")
                continue

            if number > total_applications:
                print("Completed applications cannot exceed total applications.")
                continue

            return number

        except ValueError:
            print("Please enter a valid number.")

project_name = input("Enter project name: ")
applications = get_positive_number("Enter total applications: ")
completed = get_completed_number("Enter completed applications: ", applications)
remaining = applications - completed
progress = round(calculate_progress(completed, applications), 2)
status = get_status(completed, applications)

project = {
    "name": project_name,
    "applications": applications,
    "completed": completed,
    "remaining": remaining,
    "progress": progress,
    "status": status
}

print(project)

try:
    with open("projects.json", "r") as file:
        projects = json.load(file)

except FileNotFoundError:
    projects = []

projects.append(project)

with open("projects.json", "w") as file:
    json.dump(projects, file, indent=4)