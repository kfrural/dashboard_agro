import { useEffect, useState } from "react";
import { api } from "../services/api";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from "recharts";

export function Dashboard() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    api.get("/clima").then((res) => setData(res.data));
  }, []);

  if (!data) return <p>Carregando...</p>;

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Clima Atual - Juiz de Fora</h1>
      <p>Temperatura: {data.main.temp} °C</p>
      <p>Umidade: {data.main.humidity}%</p>
      <p>Vento: {data.wind.speed} km/h</p>
    </div>
  );
}
