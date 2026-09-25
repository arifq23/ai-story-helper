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

print("Project:", project_name)
print("Applications:", applications)
print("Completed:", completed)
remaining = applications - completed
print("Remaining:", remaining)
progress = calculate_progress(completed, applications)
print("Progress:", f"{progress:.2f}%")
status = get_status(completed, applications)
print("Status:", status)