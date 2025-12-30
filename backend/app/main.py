from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import time

app = FastAPI(title="Pokemon Search Engine API")

# =========================
# ✅ CORS CONFIG
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# 🔹 In-memory Cache
# =========================
CACHE = {}
CACHE_TTL = 300        # 5 minutes
MAX_CACHE_SIZE = 100


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/pokemon/{name}")
def get_pokemon(name: str):
    key = name.lower()
    now = time.time()

    # =========================
    # ✅ Check Cache
    # =========================
    if key in CACHE:
        data, timestamp = CACHE[key]
        if now - timestamp < CACHE_TTL:
            return data
        else:
            del CACHE[key]

    # =========================
    # 🔹 Fetch from PokeAPI
    # =========================
    url = f"https://pokeapi.co/api/v2/pokemon/{key}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    raw = response.json()

    data = {
        "id": raw["id"],
        "name": raw["name"],
        "height": raw["height"],
        "weight": raw["weight"],
        "types": [t["type"]["name"] for t in raw["types"]],
        "abilities": [a["ability"]["name"] for a in raw["abilities"]],
        "stats": {
            s["stat"]["name"]: s["base_stat"]
            for s in raw["stats"]
        },
        "sprite": raw["sprites"]["front_default"],
    }

    # =========================
    # ✅ Cache Management
    # =========================
    if len(CACHE) >= MAX_CACHE_SIZE:
        CACHE.pop(next(iter(CACHE)))

    CACHE[key] = (data, now)
    return data
