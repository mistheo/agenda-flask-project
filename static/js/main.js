const modal = document.querySelector("#add-date");
const overlay = document.querySelector(".overlay");
const openModalBtn = document.querySelector("#btn-show-popup");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};


const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

overlay.addEventListener("click", closeModal);
openModalBtn.addEventListener("click", openModal);

