export default function PokemonCard({ data }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: 20 }}>
      <h2>{data.name.toUpperCase()}</h2>
      <img src={data.sprite} />
      <p>Types: {data.types.join(", ")}</p>
      <p>Abilities: {data.abilities.join(", ")}</p>
      <ul>
        {Object.entries(data.stats).map(([k, v]) => (
          <li key={k}>{k}: {v}</li>
        ))}
      </ul>
    </div>
  );
}
