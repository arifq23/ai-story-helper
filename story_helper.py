def analyse_story(story):
    score = 0

    story_lower = story.lower()

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
    
    return score

print("AI STORY HELPER")
print("----------------")

story = input("Enter your user story: ")
print()
print("Your Story:")
print(story)
words = story.split()
print("Characters:", len(story))
print("Words:", len(words))
score = analyse_story(story)
print("Story Score:", score, "/ 3")

role_position = story.lower().find("as a")
want_position = story.lower().find("i want")
benefit_position = story.lower().find("so that")

print("Role position:", role_position)
print("Goal position:", want_position)
print("Benefit position:", benefit_position)

role = story[role_position + len("as a"):want_position]
goal = story[want_position + len("i want"):benefit_position]
benefit = story[benefit_position + len("so that"):]

print("Role:", role.strip())
print("Goal:", goal.strip())
print("Benefit:", benefit.strip())
