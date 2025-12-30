export default function PokemonCard({ data }) {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: 20,
        marginTop: 20,
        borderRadius: 8,
        maxWidth: 400
      }}
    >
      <h2>{data.name.toUpperCase()}</h2>

      <img src={data.sprite} alt={data.name} />

      <p>
        <b>Types:</b> {data.types.join(", ")}
      </p>

      <p>
        <b>Abilities:</b> {data.abilities.join(", ")}
      </p>

      <h4>Stats</h4>
      <ul>
        {Object.entries(data.stats).map(([key, value]) => (
          <li key={key}>
            {key}: {value}
          </li>
        ))}
      </ul>
    </div>
  );
}
