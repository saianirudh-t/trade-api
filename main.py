import os
from fastapi import FastAPI, Depends, HTTPException, Header
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
    service = MarketService()
    report = await service.generate_report(sector)
    return {"status": "success", "report": report}