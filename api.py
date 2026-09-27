from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from story_analyser import analyse_story
from ai_service import enhance_story_with_ai
from typing import List

app = FastAPI()

class StoryRequest(BaseModel):
    story: str

class StoryAnalysis(BaseModel):
    role: str
    goal: str
    benefit: str
    score: int
    is_valid: bool
    validation_errors: list[str]


class AnalysisResponse(BaseModel):
    status: str
    analysis: StoryAnalysis


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Story Helper API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/analyse-story", response_model=AnalysisResponse)
def analyse_story_endpoint(request: StoryRequest):

    analysis = analyse_story(request.story)

    return {
        "status": "success",
        "analysis": analysis
    }

@app.post(
    "/enhance-story",
    responses={
        502: {
            "description": "Upstream AI service error"
        }
    }
)
def enhance_story_endpoint(request: StoryRequest):

    ai_result = enhance_story_with_ai(request.story)

    if ai_result["status"] == "success":
        return {
            "status": "success",
            "enhancement": ai_result["message"]
        }

    raise HTTPException(
    status_code=502,
    detail=ai_result["message"]
    )