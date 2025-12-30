export async function fetchPokemon(name) {
  const res = await fetch(`http://localhost:8000/api/pokemon/${name}`);
  if (!res.ok) throw new Error("Pokemon not found");
  return res.json();
}
