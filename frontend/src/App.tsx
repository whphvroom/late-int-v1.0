
import { useState } from 'react';
import { sendChat, sendChatSpeed, saveQA, getSavedQA } from './api';

export default function App() {
  const [message, setMessage] = useState('');
  const [answer, setAnswer] = useState('');
  const [speedMode, setSpeedMode] = useState(false);
  const [saved, setSaved] = useState<Array<{question:string; answer:string}>>([]);

  async function onAsk(e: React.FormEvent) {
    e.preventDefault();
    if (!message.trim()) return;
    setAnswer('…thinking');
    try {
      const res = speedMode ? await sendChatSpeed(message) : await sendChat(message);
      setAnswer(res.response);
    } catch {
      setAnswer('Error contacting server.');
    }
  }

  async function onSave() {
    if (!message || !answer) return;
    try { await saveQA(message, answer); alert('Saved!'); }
    catch { alert('Save failed'); }
  }

  async function onReview() {
    try { setSaved(await getSavedQA()); }
    catch { alert('Load failed'); }
  }

  return (
    <div style={{ maxWidth: 720, margin: '40px auto', fontFamily: 'system-ui, -apple-system' }}>
      <h1>Late — Internal v1.0</h1>

      <label style={{ display: 'block', margin: '8px 0' }}>
        <input type="checkbox" checked={speedMode} onChange={(e) => setSpeedMode(e.target.checked)} />{' '}
        Speed Mode
      </label>

      <form onSubmit={onAsk} style={{ display: 'flex', gap: 8 }}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask anything…"
          style={{ flex: 1, padding: '10px', border: '1px solid #ddd', borderRadius: 8 }}
        />
        <button type="submit" style={{ padding: '10px 16px', borderRadius: 8 }}>Ask</button>
      </form>

      {answer && (
        <div style={{ marginTop: 16, padding: 12, background: '#f8f8f8', borderRadius: 8 }}>
          <div style={{ fontWeight: 600, marginBottom: 8 }}>Answer</div>
          <div style={{ whiteSpace: 'pre-wrap' }}>{answer}</div>
          <button onClick={onSave} style={{ marginTop: 8, padding: '8px 12px', borderRadius: 8 }}>
            ⭐ Save
          </button>
        </div>
      )}

      <div style={{ marginTop: 24 }}>
        <button onClick={onReview} style={{ padding: '8px 12px', borderRadius: 8 }}>
          📁 Review Saved
        </button>

        {saved.length > 0 && (
          <div style={{ marginTop: 12, display: 'grid', gap: 10 }}>
            {saved.map((s, i) => (
              <div key={i} style={{ padding: 12, border: '1px solid #eee', borderRadius: 8 }}>
                <div style={{ fontWeight: 600 }}>Q:</div>
                <div>{s.question}</div>
                <div style={{ fontWeight: 600, marginTop: 6 }}>A:</div>
                <div>{s.answer}</div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
