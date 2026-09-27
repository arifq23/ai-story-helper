project = "Mainframe Modernisation"
applications = 50
completed = 25
remaining = applications - completed
progress = (completed/applications)*100

streams = [
    "FRS",
    "PBS",
    "Q2B",
    "Patterns",
    "Agentic Lumos",
    "Application Assessment"
]

print("Project:", project)
print("Total Applications:", applications)
print("Completed:", completed)
print("Remaining:", remaining)
print("Progress:", f"{progress:.2f}%")

print("Streams:")
for stream in streams:
    print(stream)

if completed == applications:
    print("All applications completed")
elif completed > applications:
    print("Something is wrong")
else:
    print("Work still remaining")