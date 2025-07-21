// edu.js - EduHack AI Tools

const topicInput = document.querySelectorAll('input')[0];
const quizInput = document.querySelectorAll('input')[1];
const summaryBox = document.querySelectorAll('div')[1];
const quizBox = document.querySelectorAll('div')[3];

document.querySelectorAll('button')[0].onclick = async () => {
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

document.querySelectorAll('button')[1].onclick = async () => {
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
