// edu.js - EduHack AI Tools

const topicInput = document.getElementById('edu-topic');
const quizInput = document.getElementById('quiz-topic');
const zeroclickInput = document.getElementById('zeroclick-url');

const summaryBox = document.getElementById('summary-result');
const quizBox = document.getElementById('quiz-result');
const zeroclickBox = document.getElementById('zeroclick-result');

document.getElementById('summary-btn').onclick = async () => {
  const topic = topicInput.value.trim();
  if (!topic) return;

  summaryBox.textContent = '📚 Generating summary...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/edu/summary', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic })
    });
    const data = await res.json();
    summaryBox.textContent = data.summary || 'No summary found.';
  } catch (err) {
    summaryBox.textContent = 'Error fetching summary.';
    console.error(err);
  }
};

document.getElementById('quiz-btn').onclick = async () => {
  const quizTopic = quizInput.value.trim();
  if (!quizTopic) return;

  quizBox.textContent = '📝 Generating quiz...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/edu/quiz', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic: quizTopic })
    });
    const data = await res.json();
    quizBox.textContent = data.quiz || 'No quiz found.';
  } catch (err) {
    quizBox.textContent = 'Error generating quiz.';
    console.error(err);
  }
};

document.getElementById('zeroclick-btn').onclick = async () => {
  const url = zeroclickInput.value.trim();
  if (!url) return;

  zeroclickBox.textContent = '🛡️ Scanning link for threats...';

  try {
    const res = await fetch('https://nova-backend.onrender.com/api/edu/zeroclick', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    const data = await res.json();
    zeroclickBox.textContent = data.analysis || 'No threats found.';
  } catch (err) {
    zeroclickBox.textContent = 'Error analyzing link.';
    console.error(err);
  }
};
