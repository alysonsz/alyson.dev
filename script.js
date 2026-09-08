const command = "portfolio --inspect";
const commandNode = document.querySelector("#typed-command");
const outputNode = document.querySelector("#terminal-output");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function runTerminal() {
  if (reduceMotion || !commandNode) {
    outputNode?.classList.add("visible");
    return;
  }

  commandNode.textContent = "";
  let index = 0;
  const timer = window.setInterval(() => {
    commandNode.textContent += command[index];
    index += 1;
    if (index === command.length) {
      window.clearInterval(timer);
      window.setTimeout(() => outputNode?.classList.add("visible"), 280);
    }
  }, 70);
}

const observer = new IntersectionObserver(
  (entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  }),
  { threshold: 0.12 }
);

document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
document.querySelector("#year").textContent = new Date().getFullYear();
runTerminal();
