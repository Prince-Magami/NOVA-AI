// typing.js

document.addEventListener("DOMContentLoaded", () => {
  const typingTargets = document.querySelectorAll(".typing-effect");

  typingTargets.forEach((target) => {
    const text = target.getAttribute("data-text");
    let index = 0;

    function typeChar() {
      if (index < text.length) {
        target.textContent += text.charAt(index);
        index++;
        setTimeout(typeChar, 60);
      }
    }

    typeChar();
  });
});
