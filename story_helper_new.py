def analyse_story(story):
    score = 0
    is_valid = False
    validation_errors = []

    story_lower = story.lower()

    role = ""
    goal = ""
    benefit = ""

    role_position = story.lower().find("as a")
    want_position = story.lower().find("i want")
    benefit_position = story.lower().find("so that")

    if (
    role_position != -1
    and want_position != -1
    and benefit_position != -1
    and role_position < want_position < benefit_position):
        is_valid = True

    if is_valid:
        role = story[role_position + len("as a"):want_position].strip(" ,")
        goal = story[want_position + len("i want"):benefit_position].strip()
        benefit = story[benefit_position + len("so that"):].strip()

    if "as a" in story_lower:
        print("Role section: Found")
        score += 1
    else:
        print("Role section: Missing - consider adding 'As a <role>'")
        validation_errors.append("Role section is missing")

    if "i want" in story_lower:
        print("Goal section: Found")
        score += 1
    else:
        print("Goal section: Missing - consider adding 'I want to <goal>'")
        validation_errors.append("Goal section is missing")

    if "so that" in story_lower:
        print("Benefit section: Found")
        score += 1
    else:
        print("Benefit section: Missing - consider adding 'So that <benefit>'")
        validation_errors.append("Benefit section is missing")

    if score == 3 and not is_valid:
        print("Story structure: Invalid - expected 'As a' -> 'I want' -> 'So that'")
        validation_errors.append("Story sections are in the wrong order")
    
    analysis = {
        "role": role.strip(),
        "goal": goal.strip(),
        "benefit": benefit.strip(),
        "score": score,
        "is_valid": is_valid,
        "validation_errors": validation_errors
        }

    return analysis

def generate_acceptance_criteria(analysis):

    if not analysis["is_valid"]:
        return []

    given = f"Given I am a {analysis['role']}"
    when = f"When I want {analysis['goal']}"
    then = f"Then {analysis['benefit']}"

    criterion = {
        "given": given,
        "when": when,
        "then": then
    }

    criterion_2 = {
        "given": "Given the requested action is available",
        "when": f"When the user attempts {analysis['goal']}",
        "then": f"Then {analysis['benefit']}"
    }
    acceptance_criteria = [
        criterion,
        criterion_2
    ]

    return acceptance_criteria

def generate_test_cases(analysis):

    happy_path = {
        "type": "Happy Path",
        "scenario": f"User attempts {analysis['goal']}",
        "expected_result": f"{analysis['benefit']}"
    }

    edge_case = {
    "type": "Edge Case",
    "scenario": "The requested action receives unusual or unsupported input",
    "expected_result": "The system handles the unusual input without crashing"
    }

    error_case = {
    "type": "Error Case",
    "scenario": "The requested action fails due to an error",
    "expected_result": "The system displays an appropriate error message"
    }

    validation_case = {
    "type": "Validation Case",
    "scenario": "The user story is incomplete or missing required sections",
    "expected_result": "The system identifies the missing story sections"
    }

    if analysis["is_valid"]:
        test_cases = [
        happy_path,
        edge_case,
        error_case
        ]

    else:
        test_cases = []

        for error in analysis["validation_errors"]:
            validation_case = {
            "type": "Validation Case",
            "scenario": error,
            "expected_result": f"The system identifies: {error}"
            }

            test_cases.append(validation_case)

    return test_cases

print("AI STORY HELPER")
print("----------------")
with open("story.txt", "r") as file:
    story = file.read()
print("Your Story:")
print(story)

story_analysis = analyse_story(story)

acceptance_criteria = generate_acceptance_criteria(story_analysis)
test_cases = generate_test_cases(story_analysis)

print()
print("ACCEPTANCE CRITERIA")
print("-------------------")

if not acceptance_criteria:
    print("Cannot generate acceptance criteria.")

    for error in story_analysis["validation_errors"]:
        print("-", error)

else:
    for number, criterion in enumerate(acceptance_criteria, start=1):
        print()
        print("Criterion", number)
        print(criterion["given"])
        print(criterion["when"])
        print(criterion["then"])

print()
print("TEST CASES")
print("-------------------")

for number, test_case in enumerate(test_cases, start=1):
    print()
    print("Test Case", number)
    print("Type:", test_case["type"])
    print("Scenario:", test_case["scenario"])
    print("Expected Result:", test_case["expected_result"])