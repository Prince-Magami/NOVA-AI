// finance.js - TailorAI Tools

const budgetInput = document.querySelectorAll('input')[0];
const careerInput = document.querySelectorAll('input')[1];
const budgetOutput = document.querySelectorAll('div')[1];
const careerOutput = document.querySelectorAll('div')[3];

document.querySelectorAll('button')[0].onclick = async () => {
  const budget = budgetInput.value.trim();
  if (!budget) return;

  budgetOutput.textContent = '📊 Calculating plan...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/finance/budget', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ budget })
    });
    const data = await res.json();
    budgetOutput.textContent = data.plan || 'Could not generate plan.';
  } catch (err) {
    budgetOutput.textContent = 'Error generating budget.';
    console.error(err);
  }
};

document.querySelectorAll('button')[1].onclick = async () => {
  const interests = careerInput.value.trim();
  if (!interests) return;

  careerOutput.textContent = '🧠 Matching careers...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/finance/career', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ interests })
    });
    const data = await res.json();
    careerOutput.textContent = data.career || 'No suggestions found.';
  } catch (err) {
    careerOutput.textContent = 'Error suggesting careers.';
    console.error(err);
  }
};
