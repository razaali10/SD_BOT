
# SD Bot API (Causal Relationship Extractor)

This API accepts a paragraph/system description and extracts causal relationships in the format:

```
[Cause Variable] → [Effect Variable] (+/-)
```

## Features
- Powered by GPT-4-Turbo
- Hosted on Render.com
- Simple FastAPI server

## Setup Instructions

1. Clone this repository.
2. Create a `.env` file with your OpenAI API key:
    ```
    OPENAI_API_KEY=your-openai-api-key-here
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run locally:
    ```
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

## Deploying to Render

1. Push the code to GitHub.
2. Connect your GitHub repository to Render.com.
3. Create a new "Web Service":
    - Environment: Python 3.11
    - Start command: `uvicorn app:app --host 0.0.0.0 --port 10000`
4. Set environment variable:
    - Key: `OPENAI_API_KEY`
    - Value: `your-openai-api-key`
5. Deploy!

## API Endpoint

**POST /parse**

Input:
```json
{
  "text": "your paragraph here"
}
```

Output:
```json
{
  "causal_relationships": [
    "A → B (+)",
    "B → C (-)"
  ]
}
```
