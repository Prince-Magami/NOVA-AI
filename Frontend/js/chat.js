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
const backendUrl = "https://nova-ai-5-sku5.onrender.com/"; 

async function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const res = await fetch(backendUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ prompt: message }),
        });

        const data = await res.json();
        addMessage(data.response || "[No response received]", "bot");
    } catch (err) {
        addMessage("[Server Error] " + err.message, "bot");
    }
}


// 🧠 Event Listeners
sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});
