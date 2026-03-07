import os
import httpx

class MarketService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        # Uses the stable 2.5 Flash endpoint from .env
        self.url = f"{os.getenv('GEMINI_ENDPOINT')}?key={self.api_key}"

    async def generate_report(self, sector: str):
        # Step 1: Simulated Data Collection (Core Requirement)
        market_context = f"Current trends for {sector} in India: Growth in exports and new policy support."
        
        # Step 2: Gemini 2.5 Flash Payload
        payload = {
            "contents": [{
                "parts": [{"text": f"Create a markdown market report for: {sector}. Context: {market_context}"}]
            }],
            "system_instruction": {"parts": [{"text": os.getenv("GEMINI_SYSTEM_PROMPT")}]}
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.url, json=payload, timeout=30.0)
                response.raise_for_status()
                data = response.json()
                
                # Extracting content from the standard response structure
                return data['candidates'][0]['content']['parts'][0]['text']
            except httpx.HTTPStatusError as e:
                return f"### API Error\nStatus: {e.response.status_code}\nDetails: {e.response.text}"
            except Exception as e:
                return f"### System Error\nCould not generate report: {str(e)}"