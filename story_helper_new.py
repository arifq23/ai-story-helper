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
        role = story[role_position + len("as a"):want_position].strip()

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




print("AI STORY HELPER")
print("----------------")
story = input("Enter your user story: ")

print("Your Story:")
print(story)

story_analysis = analyse_story(story)

print()
print("STORY ANALYSIS")
print("----------------")

print("Role:", story_analysis["role"])
print("Goal:", story_analysis["goal"])
print("Benefit:", story_analysis["benefit"])
print("Score:", story_analysis["score"], "/ 3")
