// typing.js - Typing Effect Utility

function typeEffect(element, text, speed = 50) {
  let i = 0;
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  element.innerHTML = '';
  type();
}


