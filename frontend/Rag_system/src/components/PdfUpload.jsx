import { useState } from "react";
import api from "../services/api";

function PdfUpload() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const uploadFile = async () => {
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await api.post(
                "/upload-pdf",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data",
                    },
                }
            );

            setMessage(
                `${res.data.chunks_created} chunks indexed`
            );
        } catch {
            setMessage("Upload failed");
        }
    };

    return (
        <div className="card">
            <h2>Upload PDF</h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <button onClick={uploadFile}>
                Upload
            </button>

            <p>{message}</p>
        </div>
    );
}

export default PdfUpload;