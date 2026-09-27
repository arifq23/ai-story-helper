from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()

class StoryEnhancement(BaseModel):
    improved_story: str
    suggestions: List[str]
    acceptance_criteria: List[str]
    edge_cases: List[str]

def enhance_story_with_ai(story):
    try:
        client = OpenAI()

        response = client.responses.parse(
            model="gpt-6-luna",
            instructions=(
                "You are a business analyst helping improve user stories. "
                "Review the user story and provide concise suggestions for improvement. "
                "Focus on clarity, role, goal, business benefit, acceptance criteria, "
                "edge cases, and missing information."
            ),
            input=story,
            text_format=StoryEnhancement
        )
        enhancement = response.output_parsed
        return {
            "status": "success",
            "message": enhancement,
            "original_story": story.strip()
        }
    except Exception as error:
        return {
            "status": "error",
            "message": str(error),
            "original_story": story.strip()
        }