def analyse_story(story):
    score = 0

    story_lower = story.lower()

    role = ""
    goal = ""
    benefit = ""

    role_position = story.lower().find("as a")
    want_position = story.lower().find("i want")
    benefit_position = story.lower().find("so that")

    if role_position != -1 and want_position != -1:
        role = story[role_position + len("as a"):want_position].strip(" ,")
    if want_position != -1 and benefit_position != -1:
        goal = story[want_position + len("i want"):benefit_position].strip()

    if benefit_position != -1:
        benefit = story[benefit_position + len("so that"):].strip()

    if "as a" in story_lower:
        print("Role section: Found")
        score += 1
    else:
        print("Role section: Missing - consider adding 'As a <role>'")

    if "i want" in story_lower:
        print("Goal section: Found")
        score += 1
    else:
        print("Goal section: Missing - consider adding 'I want to <goal>'")

    if "so that" in story_lower:
        print("Benefit section: Found")
        score += 1
    else:
        print("Benefit section: Missing - consider adding 'So that <benefit>'")

    analysis = {
        "role": role.strip(),
        "goal": goal.strip(),
        "benefit": benefit.strip(),
        "score": score}

    return analysis

def generate_acceptance_criteria(analysis):

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


print("AI STORY HELPER")
print("----------------")
story = input("Enter your user story: ")
print("Your Story:")
print(story)

story_analysis = analyse_story(story)

acceptance_criteria = generate_acceptance_criteria(story_analysis)

print()
print("ACCEPTANCE CRITERIA")
print("-------------------")

for number, criterion in enumerate(acceptance_criteria, start=1):
    print()
    print("Criterion", number)
    print(criterion["given"])
    print(criterion["when"])
    print(criterion["then"])
