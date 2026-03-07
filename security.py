from fastapi import Header, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

async def validate_api_key(x_api_key: str = Header(...)):
    # Simple check for demonstration [cite: 23]
    if x_api_key != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True