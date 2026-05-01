import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def analyze_file(filename, content=""):
    prompt = f"""
    You are a file organization assistant.

    Analyze this file:

    Filename: {filename}

    Extracted content:
    {content}

    Your task:
    1. Suggest category
    2. Suggest clean filename

    Return ONLY in this format:
    Category: <category>
    Filename: <clean filename>
    """

    result = ask_ai(prompt)

    name = "unknown"
    category = "Other"

    for line in result.split("\n"):
        line = line.strip().lower()

        if line.startswith("filename:"):
            name = line.split("filename:")[1].strip()

        if line.startswith("category:"):
            category = line.split("category:")[1].strip()

    return name, category