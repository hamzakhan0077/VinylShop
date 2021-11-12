/* Hides the body scrollbar */

//  body element
const body = document.body;
// checkbox element
const hamburgerToggler = document.querySelector(".toggler");
//  event listener to the hamburger 
hamburgerToggler.addEventListener("change", (e) => {
  e.target.checked
    ? (body.style.overflowY = "hidden")
    : (body.style.overflowY = "scroll");
});
