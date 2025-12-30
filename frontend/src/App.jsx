import { useState } from "react";
import { fetchPokemon } from "./api";

function App() {
  const [name, setName] = useState("");
  const [pokemon, setPokemon] = useState(null);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    setError("");
    setPokemon(null);

    try {
      const data = await fetchPokemon(name.toLowerCase());
      setPokemon(data);
    } catch (err) {
      setError("Pokemon not found");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Pokemon Search Engine</h1>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter Pokemon name"
      />
      <button onClick={handleSearch}>Search</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {pokemon && (
        <div>
          <h2>{pokemon.name.toUpperCase()}</h2>
          <img src={pokemon.sprite} alt={pokemon.name} />
          <p>Height: {pokemon.height}</p>
          <p>Weight: {pokemon.weight}</p>
          <p>Types: {pokemon.types.join(", ")}</p>

          <h3>Stats</h3>
          <ul>
            {Object.entries(pokemon.stats).map(([k, v]) => (
              <li key={k}>
                {k}: {v}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
