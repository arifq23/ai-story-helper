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