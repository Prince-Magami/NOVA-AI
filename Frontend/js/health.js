// health.js - MediSeal + MedTranslate + Medical Q&A

const symptomInput = document.getElementById('symptom-input');
const symptomResult = document.getElementById('symptom-result');

const sourceLang = document.getElementById('source-lang');
const targetLang = document.getElementById('target-lang');
const translatedResult = document.getElementById('translated-result');

const chatInput = document.getElementById('health-chat-input');
const chatOutput = document.getElementById('health-chat-output');

const voiceTranslateBtn = document.getElementById('voice-translate-btn');

// 🎯 Symptom Checker
document.getElementById('symptom-btn').onclick = async () => {
  const symptoms = symptomInput.value.trim();
  if (!symptoms) return;

  symptomResult.textContent = '🧠 Analyzing your symptoms...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/health/symptoms', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symptoms })
    });
    const data = await res.json();
    symptomResult.textContent = data.result || 'Couldn’t find a matching diagnosis.';
  } catch (err) {
    symptomResult.textContent = '⚠️ Error processing your request.';
    console.error(err);
  }
};

// 🌍 Voice Input + Translation
voiceTranslateBtn.onclick = async () => {
  translatedResult.textContent = '🎙️ Listening for speech...';

  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = sourceLang.value === 'pcm' ? 'en-US' : sourceLang.value;
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.start();

  recognition.onresult = async (event) => {
    const spokenText = event.results[0][0].transcript;
    translatedResult.textContent = `🔄 Translating: "${spokenText}"...`;

    try {
      const res = await fetch('https://nova-backend.onrender.com/api/health/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: spokenText,
          from: sourceLang.value,
          to: targetLang.value
        })
      });
      const data = await res.json();
      translatedResult.textContent = data.translated || '⚠️ Translation failed.';
    } catch (err) {
      translatedResult.textContent = '⚠️ Could not complete translation.';
      console.error(err);
    }
  };

  recognition.onerror = (event) => {
    translatedResult.textContent = '🎙️ Voice recognition failed.';
    console.error(event.error);
  };
};

// 💬 Medical Q&A Chat
document.getElementById('health-chat-btn').onclick = async () => {
  const question = chatInput.value.trim();
  if (!question) return;

  chatOutput.textContent = '🤖 Thinking...';
  chatInput.value = '';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/health/qa', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    });
    const data = await res.json();
    chatOutput.textContent = data.answer || 'No answer found.';
  } catch (err) {
    chatOutput.textContent = '⚠️ Error fetching answer.';
    console.error(err);
  }
};
