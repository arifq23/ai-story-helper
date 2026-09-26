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