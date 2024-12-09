// Toggle for the top-navigation bar for small screens
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger-menu');
    const navContainer = document.querySelector('.nav-container');
    hamburger.addEventListener('click', function() {
        navContainer.classList.toggle('nav-active');
    });
});
