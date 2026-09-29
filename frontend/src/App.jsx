import { useState } from 'react';

function App() {
    const [textInput, setTextInput] = useState('');
    const [aiOutput, setAiOutput] = useState('');
    const [working, setWorking] = useState(false);

    const queryBackend = async (e) => {
        e.preventDefault();
        if (!textInput.trim()) return;

        setWorking(true);
        setAiOutput('');

        try {
            const serverResponse = await fetch('/api/generate', {
                method: 'POST', // Must be explicitly 'POST' in uppercase
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: textInput }), // Must match your QueryPayload object
            });

            if (!serverResponse.ok) throw new Error('Backend failed to return response.');

            const parsedData = await serverResponse.json();
            setAiOutput(parsedData.result);
        } catch (err) {
            setAiOutput(`Failed: ${err.message}`);
        } finally {
            setWorking(false);
        }
    };

    return (
        <div style={{ maxWidth: '650px', margin: '60px auto', padding: '24px', fontFamily: 'system-ui' }}>
            <h3>FastAPI & React Unified Solution Template</h3>
            <form onSubmit={queryBackend}>
                <textarea
                    rows="4"
                    style={{ width: '100%', padding: '12px', fontSize: '16px', borderRadius: '4px' }}
                    placeholder="Ask Ollama via FastAPI backend..."
                    value={textInput}
                    onChange={(e) => setTextInput(e.target.value)}
                />
                <button type="submit" disabled={working} style={{ marginTop: '8px', padding: '10px 20px', cursor: 'pointer' }}>
                    {working ? 'Processing via Ollama...' : 'Submit Prompt'}
                </button>
            </form>

            {aiOutput && (
                <div style={{ marginTop: '24px', padding: '16px', backgroundColor: '#f5f5f5', borderRadius: '4px', borderLeft: '4px solid #007acc' }}>
                    <strong>Ollama Text Generation:</strong>
                    <p style={{ whiteSpace: 'pre-wrap', margin: '8px 0 0' }}>{aiOutput}</p>
                </div>
            )}
        </div>
    );
}

export default App;
