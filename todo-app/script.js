const STORAGE_KEY = "todo-app.tasks";

const form = document.getElementById("new-task-form");
const input = document.getElementById("new-task-input");
const list = document.getElementById("task-list");
const emptyState = document.getElementById("empty-state");
const count = document.getElementById("count");
const clearCompleted = document.getElementById("clear-completed");
const filterButtons = document.querySelectorAll(".filter");

let tasks = load();
let filter = "all";

function load() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return Array.isArray(stored) ? stored : [];
  } catch {
    return [];
  }
}

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function visibleTasks() {
  if (filter === "active") return tasks.filter((task) => !task.completed);
  if (filter === "completed") return tasks.filter((task) => task.completed);
  return tasks;
}

function render() {
  const shown = visibleTasks();
  list.textContent = "";

  for (const task of shown) {
    const item = document.createElement("li");
    item.className = task.completed ? "task completed" : "task";
    item.dataset.id = task.id;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.setAttribute("aria-label", `Mark "${task.title}" as completed`);

    const title = document.createElement("span");
    title.className = "task-title";
    title.textContent = task.title;

    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "delete";
    remove.textContent = "Delete";
    remove.setAttribute("aria-label", `Delete "${task.title}"`);

    item.append(checkbox, title, remove);
    list.append(item);
  }

  const remaining = tasks.filter((task) => !task.completed).length;
  count.textContent = `${remaining} ${remaining === 1 ? "task" : "tasks"} left`;
  emptyState.hidden = shown.length > 0;
  clearCompleted.hidden = tasks.length === remaining;
}

function addTask(title) {
  tasks.push({ id: Date.now().toString(36), title, completed: false });
  save();
  render();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (!title) return;
  addTask(title);
  input.value = "";
  input.focus();
});

list.addEventListener("click", (event) => {
  const item = event.target.closest(".task");
  if (!item) return;

  if (event.target.matches(".delete")) {
    tasks = tasks.filter((task) => task.id !== item.dataset.id);
    save();
    render();
  }
});

list.addEventListener("change", (event) => {
  const item = event.target.closest(".task");
  if (!item || !event.target.matches('input[type="checkbox"]')) return;

  const task = tasks.find((candidate) => candidate.id === item.dataset.id);
  if (!task) return;

  task.completed = event.target.checked;
  save();
  render();
});

for (const button of filterButtons) {
  button.addEventListener("click", () => {
    filter = button.dataset.filter;
    for (const other of filterButtons) {
      other.classList.toggle("is-active", other === button);
    }
    render();
  });
}

clearCompleted.addEventListener("click", () => {
  tasks = tasks.filter((task) => !task.completed);
  save();
  render();
});

render();
