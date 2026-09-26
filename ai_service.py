from openai import OpenAI

def enhance_story_with_ai(story):

    client = OpenAI()

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=(
            "You are a business analyst helping improve user stories. "
            "Review the user story and provide concise suggestions for improvement. "
            "Focus on clarity, role, goal, business benefit, acceptance criteria, "
            "edge cases, and missing information."
        ),
        input=story
    )

    return {
        "status": "success",
        "message": response.output_text,
        "original_story": story.strip()
    }