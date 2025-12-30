const API_BASE = "http://127.0.0.1:8000";

export async function fetchPokemon(name) {
  const response = await fetch(`${API_BASE}/api/pokemon/${name}`);

  if (!response.ok) {
    throw new Error("Pokemon not found");
  }

  return response.json();
}
