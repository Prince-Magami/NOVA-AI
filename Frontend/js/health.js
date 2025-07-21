// health.js - MediSeal + MedTranslate Logic

const symptomInput = document.getElementById('symptom-input');
const symptomResult = document.getElementById('symptom-result');

const medInput = document.getElementById('med-translate-input');
const medOutput = document.getElementById('med-translate-output');

document.querySelectorAll('button')[0].onclick = async () => {
  const text = symptomInput.value.trim();
  if (!text) return;

  symptomResult.textContent = '🧠 Analyzing...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/health/symptoms', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symptoms: text })
    });
    const data = await res.json();
    symptomResult.textContent = data.result || 'No clear diagnosis.';
  } catch (err) {
    symptomResult.textContent = 'Error processing input.';
    console.error(err);
  }
};

document.querySelectorAll('button')[1].onclick = async () => {
  const text = medInput.value.trim();
  if (!text) return;

  medOutput.textContent = '🔄 Translating...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/health/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    medOutput.textContent = data.translated || 'Translation failed.';
  } catch (err) {
    medOutput.textContent = 'Error translating.';
    console.error(err);
  }
};
