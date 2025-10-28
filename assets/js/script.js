const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
const logo = document.getElementById('logo');

hamburger.addEventListener('click', () => {
  const isActive = navLinks.classList.contains('show');

  if (isActive) {
    navLinks.classList.remove('show');
    hamburger.classList.remove('active');
    logo.src = "assets/images/logo.png";
  } else {
    navLinks.classList.add('show');
    hamburger.classList.add('active');
    logo.src = "assets/images/logo-alt.png";
  }
});
