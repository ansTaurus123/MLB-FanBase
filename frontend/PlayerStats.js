import React, { useState } from "react";
import axios from "axios";

function PlayerStats() {
    const [playerId, setPlayerId] = useState("");
    const [stats, setStats] = useState(null);

    const fetchStats = async () => {
        const response = await axios.get(`/api/mlb/player/${playerId}`);
        setStats(response.data);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Player ID"
                onChange={(e) => setPlayerId(e.target.value)}
            />
            <button onClick={fetchStats}>Fetch Stats</button>
            {stats && <pre>{JSON.stringify(stats, null, 2)}</pre>}
        </div>
    );
}

export default PlayerStats;
