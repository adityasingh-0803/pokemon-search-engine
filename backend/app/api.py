from fastapi import APIRouter, HTTPException
from app.services.pokeapi_service import get_pokemon
import httpx

router = APIRouter(prefix="/api")

@router.get("/pokemon/{name}")
async def fetch_pokemon(name: str):
    if not name.isalpha():
        raise HTTPException(status_code=400, detail="Invalid pokemon name")

    try:
        return await get_pokemon(name)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        raise HTTPException(status_code=500, detail="External API error")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
