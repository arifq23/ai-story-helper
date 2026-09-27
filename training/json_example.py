import json

with open("project.json", "r") as file:
    projects = json.load(file)

for project in projects:
    print(
        project["name"]
    )