# Pokemon Search Engine – Backend

This is the backend service for the Pokemon Search Engine application.  
It exposes RESTful APIs to fetch Pokémon data from the public PokeAPI, with an in-memory caching layer to improve performance.

---

## 🚀 Features
- REST API built using FastAPI
- Fetches real-time Pokémon data from PokeAPI
- In-memory caching with TTL (time-to-live)
- Cache eviction to control memory usage
- Proper error handling for invalid Pokémon names
- CORS enabled for frontend integration

---

## 🛠 Tech Stack
- Python
- FastAPI
- Uvicorn
- Requests
- PokeAPI

---

## 📂 Project Structure
```bash
backend/
├── app/
│ └── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the backend server
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 🔗 API Endpoints
 ## Health Check
 ```bash
GET /
GET /health
```
## Get Pokémon by Name
 ```bash
GET /api/pokemon/{name}
```
### ⚡ Caching Strategy

- Uses in-memory dictionary cache

- Cache TTL: 5 minutes

- Evicts oldest entry when cache limit is reached

- Reduces repeated calls to external API

### 🧪 API Testing
Swagger UI is available at:
 ```bash
http://127.0.0.1:8000/docs
 ```
