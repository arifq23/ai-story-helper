import json
def build_story_report(story, analysis, acceptance_criteria, test_cases):

    report = {
        "story": story.strip(),
        "analysis": analysis,
        "acceptance_criteria": acceptance_criteria,
        "test_cases": test_cases
    }

    return report

def save_story_report(report, filename):

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

def load_story_report(filename):

    try:
        with open(filename, "r") as file:
            report = json.load(file)

        return report

    except FileNotFoundError:
        print("Error: Report file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Report file contains invalid JSON.")
        return None
