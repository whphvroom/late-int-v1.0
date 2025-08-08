
const BASE_URL = 'http://127.0.0.1:8000';

export async function sendChat(message: string) {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });
  if (!res.ok) throw new Error('Failed');
  return res.json() as Promise<{ response: string }>;
}

export async function sendChatSpeed(message: string) {
  const res = await fetch(`${BASE_URL}/chat/speed`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });
  if (!res.ok) throw new Error('Failed');
  return res.json() as Promise<{ response: string }>;
}

export async function saveQA(question: string, answer: string) {
  const res = await fetch(`${BASE_URL}/save`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, answer }),
  });
  if (!res.ok) throw new Error('Failed');
  return res.json() as Promise<{ status: string }>;
}

export async function getSavedQA() {
  const res = await fetch(`${BASE_URL}/review`);
  if (!res.ok) throw new Error('Failed');
  return res.json() as Promise<Array<{question:string; answer:string}>>;
}
