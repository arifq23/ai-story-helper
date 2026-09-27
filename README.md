# ai-story-helper

# AI Story Helper

AI Story Helper is a Python application that analyses user stories using both deterministic Python rules and generative AI.

The application can:

- Analyse the structure of a user story
- Extract the role, goal and business benefit
- Validate the user story format
- Generate acceptance criteria
- Generate test cases
- Use the OpenAI API to improve the story
- Generate AI suggestions, acceptance criteria and edge cases
- Save the complete analysis as a structured JSON report

## Project Architecture

```text
ai-story-helper/
├── story_helper.py
├── story_analyser.py
├── generators.py
├── report_manager.py
├── ai_service.py
├── requirements.txt
├── .env.example
├── .gitignore
└── story.txt
```

### Python Modules

**story_helper.py**

Main application entry point. It coordinates the complete application flow.

**story_analyser.py**

Performs deterministic analysis of the user story, including role, goal, benefit and structural validation.

**generators.py**

Generates local acceptance criteria and test cases from the deterministic story analysis.

**report_manager.py**

Builds, saves and loads the structured JSON story report.

**ai_service.py**

Connects the application to the OpenAI API and returns structured AI enhancements.

## Requirements

- Python 3
- Git
- An OpenAI API key

Python dependencies are defined in `requirements.txt`:

```text
openai
pydantic
python-dotenv
```

## Clone the Repository

```bash
git clone git@github.com:arifq23/ai-story-helper.git
cd ai-story-helper
```

## Install Python Dependencies

Run:

```bash
python3 -m pip install -r requirements.txt
```

This installs the Python packages required by the application.

## Configure the OpenAI API Key

The application reads the OpenAI API key from a local `.env` file.

Create the file from the provided template:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual API key:

```text
OPENAI_API_KEY=your_actual_api_key_here
```

Do not commit `.env` to Git.

The `.env` file is excluded through `.gitignore`.

## Provide a User Story

Edit `story.txt` and enter a user story using the following structure:

```text
As a <role>, I want <goal> so that <business benefit>.
```

Example:

```text
As a product owner, I want to assess a COBOL application so that I can understand its migration complexity.
```

## Run the Application

From the project directory, run:

```bash
python3 story_helper.py
```

The application will:

1. Read the user story
2. Perform deterministic analysis
3. Generate acceptance criteria
4. Generate test cases
5. Call the OpenAI API
6. Generate structured AI enhancements
7. Build a unified report
8. Save the report as `story_report.json`

## Output

The generated JSON report contains:

```text
story
analysis
acceptance_criteria
test_cases
ai_enhancement
```

The AI enhancement includes:

```text
improved_story
suggestions
acceptance_criteria
edge_cases
```

`story_report.json` is generated locally and is excluded from Git.

## Security

Never store an actual OpenAI API key directly in Python source code or commit it to GitHub.

The local `.env` file contains the secret API key and should remain excluded through `.gitignore`.

The `.env.example` file contains only a placeholder and can safely be committed.

## Application Flow

```text
User Story
    |
    +----------------------+
    |                      |
    v                      v
Python Analysis         OpenAI API
    |                      |
    v                      v
Deterministic          AI Enhancement
Results                   |
    |                      |
    +----------+-----------+
               |
               v
        Unified Report
               |
               v
      story_report.json
```