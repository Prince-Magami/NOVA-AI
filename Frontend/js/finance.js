// finance.js - TailorAI Logic with Voice Input & AI API

const voiceBtn = document.getElementById('voice-btn');
const voiceOutput = document.getElementById('voice-output');

const budgetInput = document.getElementById('budget-input');
const careerInput = document.getElementById('career-input');

const budgetBtn = document.getElementById('budget-btn');
const careerBtn = document.getElementById('career-btn');

const budgetOutput = document.getElementById('budget-result');
const careerOutput = document.getElementById('career-result');

// 🔊 Voice Input Logic
voiceBtn.addEventListener('click', () => {
  if (!('webkitSpeechRecognition' in window)) {
    voiceOutput.textContent = '⚠️ Voice recognition not supported in this browser.';
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-US';
  recognition.continuous = false;
  recognition.interimResults = false;

  voiceOutput.textContent = '🎤 Listening... Speak now.';

  recognition.onresult = async (event) => {
    const transcript = event.results[0][0].transcript;
    voiceOutput.textContent = `🗣️ "${transcript}"`;
    
    try {
      const res = await fetch('https://nova-backend.onrender.com/api/finance/budget', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget: transcript })
      });
      const data = await res.json();
      budgetOutput.textContent = data.plan || '⚠️ Could not generate plan from voice input.';
    } catch (err) {
      budgetOutput.textContent = '⚠️ Voice planning failed.';
      console.error(err);
    }
  };

  recognition.onerror = (e) => {
    voiceOutput.textContent = '❌ Voice recognition error.';
    console.error(e);
  };

  recognition.start();
});

// 💸 Budget Planner
budgetBtn.addEventListener('click', async () => {
  const text = budgetInput.value.trim();
  if (!text) return;

  budgetOutput.textContent = '📊 Generating your personalized budget...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/finance/budget', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ budget: text })
    });
    const data = await res.json();
    budgetOutput.textContent = data.plan || '⚠️ Could not generate plan.';
  } catch (err) {
    budgetOutput.textContent = '⚠️ Error reaching TailorAI.';
    console.error(err);
  }
});

// 👔 Career Matcher
careerBtn.addEventListener('click', async () => {
  const text = careerInput.value.trim();
  if (!text) return;

  careerOutput.textContent = '🔍 Finding careers that match you...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/finance/career', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ interests: text })
    });
    const data = await res.json();
    careerOutput.textContent = data.career || '⚠️ No matching careers found.';
  } catch (err) {
    careerOutput.textContent = '⚠️ Error contacting career AI.';
    console.error(err);
  }
});
