Trade Opportunities API

A FastAPI-based service designed to analyze Indian market sectors (e.g., pharmaceuticals, technology, agriculture) and provide structured trade opportunity insights using Google Gemini AI.
🚀 Features

    Sector Analysis: Generates structured markdown reports with current trade opportunities.

    AI Integration: Utilizes the Google Gemini 2.5 Flash model for deep market analysis.

    Security: Implements API Key authentication and input validation.

    Rate Limiting: Prevents abuse by limiting users to 5 requests per minute.

    In-Memory Storage: Lightweight session tracking without the need for an external database.

🛠️ Tech Stack

    Framework: FastAPI 

    LLM: Google Gemini 2.5 Flash 

    Environment: Python 3.12+ (venv)

    Client: Postman / cURL for testing 

📋 Setup Instructions
1. Clone & Environment
Bash

git clone <your-repo-url>
cd trade-api
python3 -m venv venv
source venv/bin/activate

2. Install Dependencies
Bash

pip install -r requirements.txt

3. Configuration (.env)

Create a .env file in the root directory and add the following:
Code snippet
    Framework: FastAPI 

    SECRET_KEY=devsecret123

    RATE_LIMIT_PER_MINUTE=5

    GEMINI_API_KEY=your_gemini_api_key_here

    GEMINI_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent

4. Run the Server
Bash

uvicorn main:app --reload

The server will start at http://127.0.0.1:8000.
🚦 API Usage
Analyze Sector

Returns a structured markdown report for a specific Indian market sector.

    URL: /analyze/{sector} 

    Method: GET 

    Headers:

        X-API-Key: devsecret123 

    Sample Request: http://127.0.0.1:8000/analyze/pharmaceuticals 

📂 Project Structure

    main.py: Entry point with FastAPI routes and rate limiting.

    services.py: Logic for data collection and Gemini AI analysis.

    security.py: Authentication and security middleware.

    .env: Sensitive environment variables (ignored by git).
