# 🧠 Pokémon Search Engine (Pokedex)

A full-stack Pokémon Search Engine that allows users to search Pokémon by name and view detailed information such as stats, types, abilities, and images.  
The system is built with a backend REST API and a frontend UI, designed to run entirely **locally**.

---

## 🚀 Key Features
- Search Pokémon by name (case-insensitive)
- Displays Pokémon image, stats, height, weight, types, and abilities
- Backend caching to improve performance for repeat searches
- Clean RESTful API design
- Simple and responsive frontend UI
- Fully local setup (as required by the assignment)

---

## 🏗️ Architecture Overview

Frontend (React + Vite) → REST API → Backend (FastAPI) → External API (PokeAPI)


---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Requests
- In-memory caching (TTL-based)

### Frontend
- React
- Vite
- JavaScript (ES6+)
- HTML & CSS

---

## 📂 Project Structure

pokemon-search-engine/
├── backend/
│ ├── app/
│ │ └── main.py
│ ├── requirements.txt
│ └── README.md
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── api.js
│ │ └── main.jsx
│ ├── index.html
│ ├── vite.config.js
│ ├── package.json
│ └── README.md
│
└── README.md


---

## ⚙️ How to Run the Project Locally

### 1️⃣ Start the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Backend URL:
```bash
http://127.0.0.1:8000
```
Swagger Docs:
```bash
http://127.0.0.1:8000/docs
```

### 2️⃣ Start the Frontend
Open a new terminal:
```bash
cd frontend
npm install
npm run dev
```
Frontend URL:
```bash
http://localhost:5173
```

### 🔗 API Endpoints
Get Pokémon by Name
```bash
GET /api/pokemon/{name}
```
Example:
```bash
GET /api/pokemon/pikachu
```

⚡ Performance Optimization (Caching)

- In-memory cache implemented in backend

- Cache TTL: 5 minutes

- Cache eviction when size limit is reached

- Reduces repeated calls to external PokeAPI

🧪 Example Pokémon to Try

- pikachu

- charizard

- mewtwo

- gengar

- lucario

📌 Notes

- Backend must be running before starting the frontend

- Designed to be simple, readable, and extensible

- Runs completely locally as required by the assignment

👤 Author

Developed as part of a technical coding challenge to demonstrate full-stack development, REST API design, and performance optimization.
