const command = "portfolio --inspect";
const commandNode = document.querySelector("#typed-command");
const outputNode = document.querySelector("#terminal-output");
const root = document.documentElement;

const supportsObserver = "IntersectionObserver" in window;
root.classList.add("motion-enabled");
requestAnimationFrame(() => {
  requestAnimationFrame(() => root.classList.add("is-loaded"));
});

function runTerminal() {
  if (!commandNode) {
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

const observer = supportsObserver ? new IntersectionObserver(
  (entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  }),
  { threshold: 0.12 }
): null;

document.querySelectorAll(".reveal").forEach((element) => {
  if (observer) observer.observe(element);
  else element.classList.add("is-visible");
});

const staggerGroups = [
  ".xyz-list",
  ".impact-list",
  ".tag-row",
  ".stack-grid"
];

staggerGroups.forEach((selector) => {
  document.querySelectorAll(selector).forEach((group) => {
    Array.from(group.children).forEach((element, index) => {
      if (observer) {
        element.classList.add("micro-reveal");
        element.style.setProperty("--reveal-delay", `${Math.min(index * 70, 350)}ms`);
        observer.observe(element);
      }
    });
  });
});

document.querySelectorAll(".timeline-item").forEach((element, index) => {
  element.style.setProperty("--reveal-delay", `${index * 90}ms`);
});

document.querySelector("#year").textContent = new Date().getFullYear();
runTerminal();
