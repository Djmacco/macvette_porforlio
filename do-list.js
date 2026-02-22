const addElement = document.getElementById("btn");
const inputElement = document.getElementById("input");
let divcontainer = document.querySelector(".display-elements");
//const items = document.getElementById('btn');

const Storage_key = "kolo";
let items = [];

function dolist() {
  divcontainer.innerHTML = null;
  for (const [idx, item] of Object.entries(items)) {
    const container = document.createElement("div");
    const text = document.createElement("span");
    text.textContent = item;

    container.appendChild(text);
    const Button = document.createElement("button");
    Button.textContent = "delete";
    container.appendChild(Button);

    const textEdit = document.createElement("button");
    textEdit.textContent = "edit";
    textEdit.className = "edit";
    divcontainer.appendChild(container);
    container.appendChild(textEdit);
    // textEdit.classList.add("edit");
    // delete button
    Button.onclick = () => delete_items(idx);
    text.style.marginRight = "10px";
    container.classList.add("container");

    const edit_btn = document.querySelectorAll(".edit");
    let count = 0;
    edit_btn.forEach((btn) => {
      btn.addEventListener("click", () => {
        count++;
        if (count >= 2) return;

        const editDIv = document.createElement("div");
        const input = document.createElement("input");
        const buttonSave = document.createElement("button");
        buttonSave.textContent = "save";

        editDIv.appendChild(input);
        editDIv.appendChild(buttonSave);
        buttonSave.addEventListener("click", () => {
          if (!input.value || input.value === "") return;
          text.textContent = input.value;
          //save_items();

          if (input.value !== "") {
            input.style.display = "none";
            buttonSave.style.display = "none";
          }
        });
        container.appendChild(editDIv);
      });
    });
  }
}
dolist();

const delete_items = (idx) => {
  items.splice(idx, 1);
  save_items();
  dolist();
};

const add_element = () => {
  let input = inputElement.value;
  if (!input) return;
  items.push(input);
  save_items();
  dolist();
  inputElement.value = "";
};

const save_items = () => {
  const items_str = JSON.stringify(items);
  localStorage.setItem(Storage_key, items_str);
  reload_items();
};
const reload_items = () => {
  const oldStorage = localStorage.getItem(Storage_key);

  if (oldStorage) items = JSON.parse(oldStorage);
  dolist();
};

addElement.addEventListener("click", add_element);

document.addEventListener("DOMContentLoaded", reload_items);
