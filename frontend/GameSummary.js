import React, { useState } from "react";
import axios from "axios";

function GameSummary() {
    const [inputText, setInputText] = useState("");
    const [summary, setSummary] = useState("");

    const summarizeText = async () => {
        try {
            const response = await axios.post("/api/llm/summarize", {
                text: inputText,
            });
            setSummary(response.data.summary);
        } catch (error) {
            console.error("Error generating summary:", error);
        }
    };

    return (
        <div>
            <h2>Game Highlights Summary</h2>
            <textarea
                placeholder="Enter game details..."
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
            />
            <button onClick={summarizeText}>Summarize</button>
            {summary && (
                <div>
                    <h3>Summary:</h3>
                    <p>{summary}</p>
                </div>
            )}
        </div>
    );
}

export default GameSummary;
