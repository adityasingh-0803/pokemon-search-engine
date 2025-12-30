import httpx
from app.cache import pokemon_cache

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

async def fetch_pokemon(name: str):
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{BASE_URL}/{name.lower()}")
        response.raise_for_status()
        return response.json()

def transform(data: dict) -> dict:
    return {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {
            s["stat"]["name"]: s["base_stat"]
            for s in data["stats"]
        },
        "sprite": data["sprites"]["front_default"]
    }

async def get_pokemon(name: str):
    if name in pokemon_cache:
        return pokemon_cache[name]

    data = await fetch_pokemon(name)
    pokemon = transform(data)
    pokemon_cache[name] = pokemon
    return pokemon
