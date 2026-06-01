import { useState } from "react";
import api from "../services/api";

function TextUpload() {
    const [text, setText] = useState("");
    const [message, setMessage] = useState("");

    const uploadText = async () => {
        try {
            const res = await api.post(
                "/upload-text",
                { text }
            );

            setMessage(
                `${res.data.chunks_created} chunks indexed`
            );

            setText("");
        } catch {
            setMessage("Failed");
        }
    };

    return (
        <div className="card">
            <h2>Add Text</h2>

            <textarea
                rows="8"
                value={text}
                onChange={(e) =>
                    setText(e.target.value)
                }
            />

            <button onClick={uploadText}>
                Index Text
            </button>

            <p>{message}</p>
        </div>
    );
}

export default TextUpload;