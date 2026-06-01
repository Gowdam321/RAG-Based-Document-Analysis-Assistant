import PdfUpload from "./components/PdfUpload";
import TextUpload from "./components/TextUpload";
import ChatBox from "./components/ChatBox";
import "./App.css";

function App() {
    return (
        <div className="container">
            <h1>RAG Assistant</h1>

            <div className="top-section">
                <PdfUpload />
                <TextUpload />
            </div>

            <ChatBox />
        </div>
    );
}

export default App;