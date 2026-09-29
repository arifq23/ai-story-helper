from story_analyser import analyse_story

def test_valid_story():
    story = (
        "As a product owner, "
        "I want to assess a COBOL application "
        "so that I can understand its migration complexity."
    )

    result = analyse_story(story)

    assert result["role"] == "product owner"
    assert result["goal"] == "to assess a COBOL application"
    assert result["score"] == 5
    assert result["is_valid"] is True
    assert result["validation_errors"] == []