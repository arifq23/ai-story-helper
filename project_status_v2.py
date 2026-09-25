def calculate_progress(completed, total):
    progress = (completed / total) * 100
    return progress

def get_status(completed, total):

    if completed == total:
        return "All applications completed"

    elif completed > total:
        return "Something is wrong"

    else:
        return "Work still remaining"

project = {
    "name": "Mainframe Modernisation",
    "applications": 50,
    "completed": 25,
    "streams": [
        "FRS",
        "PBS",
        "Q2B",
        "Patterns",
        "Agentic Lumos",
        "Application Assessment"
    ]
}

print("Project: ", project["name"])
print("Total Applications: ", project["applications"])
remaining = project["applications"] - project["completed"]
print("Completed: ", project["completed"])
print("Remaining: ", remaining)
progress = calculate_progress(project["completed"], project["applications"])
print("Progress:", f"{progress:.2f}%")
status = get_status(project["completed"], project["applications"])
print("Status:", status)
print("Streams:")
for stream in project["streams"]:
    print("-",stream)

