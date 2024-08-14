let nav = document.getElementById('nav1');
let menu = document.getElementById('menu');

menu.addEventListener('click', function() {
  if (nav.style.display == 'none') {
    nav.style.display = "block";
  } else {
    nav.style.display = "none";
  }
});
