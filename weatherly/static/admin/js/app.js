let buttonPlus = document.getElementById('notify-icon');
let optionList = document.querySelector('.option-container');
buttonPlus.addEventListener('click',ShowMenu);

function ShowMenu(){
      optionList.classList.toggle("display_none");
}
