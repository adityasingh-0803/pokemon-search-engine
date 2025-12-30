
# Pokemon Search Engine – Frontend
```md
This is the frontend application for the Pokemon Search Engine.  
It provides a simple and responsive UI to search Pokémon by name and display their details.
```
---

## 🚀 Features
```md
- Search Pokémon by name
- Displays image, stats, height, weight, and types
- Clean and minimal UI
- Integrates with backend REST API
- Handles loading and error states
```
---

## 🛠 Tech Stack
```md
- React
- Vite
- JavaScript (ES6+)
- HTML & CSS
```
---

## 📂 Project Structure
```md
frontend/
├── src/
│ ├── App.jsx
│ ├── api.js
│ └── main.jsx
├── index.html
├── vite.config.js
├── package.json
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
```bash
npm install
```
### 2️⃣ Start frontend server
```bash
npm run dev
```
### 🌐 Access Application
```bash
http://localhost:5173
```
## 🔗 Backend Dependency

Ensure the backend is running at:
```bash
http://127.0.0.1:8000
```
The frontend fetches data from:
```bash
/api/pokemon/{name}
```

## 🧪 Example Usage

- Enter pikachu, charizard, or mewtwo

- Click Search

- Pokémon details will be displayed
