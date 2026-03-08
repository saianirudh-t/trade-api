import os
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.requests import Request
from services import MarketService

load_dotenv()
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

async def verify_auth(x_api_key: str = Header(...)):
    if x_api_key != os.getenv("SECRET_KEY"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    return True

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze(request: Request, sector: str, auth: bool = Depends(verify_auth)):
    try:
        service = MarketService()
        # The service handles data collection and Gemini analysis [cite: 36, 37]
        report_content = await service.generate_report(sector)
        
        # Define the filename for the .md file 
        filename = f"{sector}_analysis.md"
        
        return PlainTextResponse(
            content=report_content,
            headers={
                "X-Status": "success",
                "X-Summary": f"Market analysis for {sector} generated successfully.",
                "Content-Disposition": f"attachment; filename={filename}"
            }
        )
    except Exception as e:
        # Proper error handling for external API failures [cite: 42, 62]
        raise HTTPException(status_code=500, detail=str(e))