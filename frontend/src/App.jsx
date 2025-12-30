import { useState } from "react";
import { fetchPokemon } from "./api";
import PokemonCard from "./components/PokemonCard";

export default function App() {
  const [name, setName] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const search = async () => {
    try {
      setError("");
      const result = await fetchPokemon(name);
      setData(result);
    } catch {
      setError("Pokemon not found");
      setData(null);
    }
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Pokemon Search</h1>
      <input onChange={e => setName(e.target.value)} />
      <button onClick={search}>Search</button>

      {error && <p>{error}</p>}
      {data && <PokemonCard data={data} />}
    </div>
  );
}
