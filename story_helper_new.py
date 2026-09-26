
from story_analyser import analyse_story
from generators import generate_acceptance_criteria, generate_test_cases
from report_manager import build_story_report, save_story_report, load_story_report
from ai_service import enhance_story_with_ai

def main():
    print("AI STORY HELPER")
    print("----------------")
    with open("story.txt", "r") as file:
        story = file.read()
    print("Your Story:")
    print(story)

    story_analysis = analyse_story(story)
    acceptance_criteria = generate_acceptance_criteria(story_analysis)
    test_cases = generate_test_cases(story_analysis)
    story_report = build_story_report(story, story_analysis, acceptance_criteria, test_cases)
    save_story_report(story_report, "story_report.json")
    loaded_report = load_story_report("story_report.json")  # Change the filename to "story_report.json" to load the correct report
    ai_result = enhance_story_with_ai(story)

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

    if loaded_report is not None:
        print()
        print("STRUCTURED STORY REPORT")
        print("-----------------------")
        print(loaded_report)

        print()
        print("LOADED REPORT")
        print("-------------")

        print("Story:", loaded_report["story"])
        print("Role:", loaded_report["analysis"]["role"])
        print("Goal:", loaded_report["analysis"]["goal"])
        print("Valid:", loaded_report["analysis"]["is_valid"])
        print()
        print("TEST CASES FROM JSON")

        for test_case in loaded_report["test_cases"]:
            print("-", test_case["type"], ":", test_case["scenario"])

        print()
        print("AI ENHANCEMENT")
        print("--------------")
        print("Status:", ai_result["status"])
        print("Message:", ai_result["message"])

if __name__ == "__main__":
    main()