// chat.js - NOVA AI Gemini Chat Logic

const chatBox = document.getElementById('chat-box');
const input = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// 🔵 Add Message to UI (Bubble Style)
function addMessage(text, isUser = true) {
  const wrapper = document.createElement('div');
  const bubble = document.createElement('div');

  wrapper.classList.add(isUser ? 'justify-start' : 'justify-end');
  bubble.className = isUser ? 'user-msg' : 'ai-msg';
  bubble.textContent = text;

  wrapper.appendChild(bubble);
  chatBox.appendChild(wrapper);

  chatBox.scrollTop = chatBox.scrollHeight;
}

// 🚀 Send to Gemini API (Backend Proxy)
async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, true);
  input.value = '';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    addMessage(data.reply || '⚠️ Sorry, I couldn’t process that.', false);
  } catch (err) {
    console.error('❌ API Error:', err);
    addMessage('⚠️ Error reaching NOVA backend.', false);
  }
}

// 🧠 Event Listeners
sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});
