Trade Opportunities API

A FastAPI-based service that analyzes market data and provides structured trade opportunity insights for specific sectors in India.
🚀 Features

    Sector Analysis: Generates structured market reports for Indian sectors (e.g., pharmaceuticals, technology, agriculture).

    AI-Powered Insights: Uses the Gemini 2.5 Flash model for deep market data analysis.

    Automatic Downloads: Returns reports as downloadable .md files directly in the response.

    Security: Implements API Key authentication and rate limiting to prevent abuse.

    Architecture: Clean separation between API, data collection, and AI logic layers.

🛠️ Tech Stack

    Backend: FastAPI

    LLM: Google Gemini 2.5 Flash 

    Rate Limiting: Slowapi 

    Environment: Python 3.12+ (managed via venv)

📋 Setup Instructions
1. Environment Setup
Bash

# Clone the repository
git clone <your-repo-url>
cd trade-api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
Install via requirements.txt file
pip install -r requirements.txt

2. Configuration (.env)

Create a .env file in the root directory and add your credentials:
Code snippet
Framework: FastAPI 

SECRET_KEY=devsecret123
RATE_LIMIT_PER_MINUTE=5
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent

3. Running the Server
Bash

uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000.
🚦 API Usage
Analyze Sector

Accepts a sector name and returns a structured markdown report for download.

    URL: /analyze/{sector}

    Method: GET

    Headers:

        X-API-Key: devsecret123

    Example: http://127.0.0.1:8000/analyze/pharmaceuticals 

🧪 Testing in Postman

    Enter the URL with a sector name.

    Add the X-API-Key to the Headers tab.

    Click Send.

    To get the file, click the Save Response (down arrow) and select Save to a file.