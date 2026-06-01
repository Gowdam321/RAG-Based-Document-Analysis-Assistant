import { useState } from "react";
import api from "../services/api";

function ChatBox() {
    const [query, setQuery] = useState("");
    const [messages, setMessages] = useState([]);

    const askQuestion = async () => {
        if (!query.trim()) return;

        const userMsg = {
            role: "user",
            content: query,
        };

        setMessages((prev) => [
            ...prev,
            userMsg,
        ]);

        try {
            const res = await api.post(
                "/query",
                {
                    query,
                }
            );

            const botMsg = {
                role: "assistant",
                content:
                    res.data.answer ||
                    JSON.stringify(res.data),
            };

            setMessages((prev) => [
                ...prev,
                botMsg,
            ]);
        } catch {
            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: "Error",
                },
            ]);
        }

        setQuery("");
    };

    const clearIndex = async () => {
        await api.delete("/clear-index");

        alert("Vector DB Cleared");
    };

    return (
        <div className="chat-card">
            <div className="chat-header">
                <h2>Ask Questions</h2>

                <button
                    className="danger"
                    onClick={clearIndex}
                >
                    Clear Index
                </button>
            </div>

            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        className={msg.role}
                    >
                        {msg.content}
                    </div>
                ))}
            </div>

            <div className="input-area">
                <input
                    value={query}
                    onChange={(e) =>
                        setQuery(e.target.value)
                    }
                    placeholder="Ask anything..."
                />

                <button onClick={askQuestion}>
                    Send
                </button>
            </div>
        </div>
    );
}

export default ChatBox;