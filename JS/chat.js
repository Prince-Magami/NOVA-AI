// chat.js - Chatbox Logic for NOVA AI

const chatBox = document.getElementById('chat-box');
const input = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// 🧠 Append user and bot messages
function addMessage(sender, text) {
  const msg = document.createElement('div');
  msg.classList.add('mb-2');
  msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// 🛰️ Send user query to backend
async function sendMessage() {
  const userText = input.value.trim();
  if (!userText) return;

  addMessage('You', userText);
  input.value = '';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userText })
    });
    const data = await res.json();
    addMessage('NOVA', data.reply || 'Sorry, I couldn’t process that.');
  } catch (err) {
    addMessage('NOVA', '⚠️ Error reaching server.');
    console.error(err);
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});
