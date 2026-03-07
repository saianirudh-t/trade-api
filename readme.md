Trade Opportunities API

A FastAPI-based service that analyzes Indian market sectors (e.g., pharmaceuticals, technology) using Google Gemini AI to provide structured trade opportunity reports.
Features

    Sector Analysis: Generates structured markdown reports for specific Indian sectors.

    AI Powered: Utilizes Gemini 1.5 Pro for deep market insights.

    Security: Implemented API Key authentication and Rate Limiting (5 requests/min).

    Clean Architecture: Separation of concerns between API, Security, and AI logic.

Setup Instructions

    Clone the repository and navigate to the project folder.

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Configure Environment:
    Create a .env file and add your credentials as seen in your configuration:
    Code snippet

    GEMINI_API_KEY=your_api_key_here
    GEMINI_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent
    SECRET_KEY=devsecret123

    Run the Application:
    Bash

    uvicorn main:app --reload

API Usage
Analyze Sector

Returns a structured markdown report for the requested sector.

    URL: /analyze/{sector} 

    Method: GET 

    Headers: X-API-Key: devsecret123 

    Example: /analyze/pharmaceuticals