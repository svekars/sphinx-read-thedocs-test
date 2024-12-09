document.addEventListener("DOMContentLoaded", function() {
    const menuLinks = document.querySelectorAll('.pytorch-right-menu a.reference.internal');

    // Function to remove 'current' class from all links
    function removeCurrentClass() {
        menuLinks.forEach(link => {
            link.classList.remove('current');
        });
    }

    // Function to add 'current' class to the active link
    function addCurrentClass() {
        removeCurrentClass();
        menuLinks.forEach(link => {
            if (window.location.hash && link.getAttribute('href') === window.location.hash) {
                link.classList.add('current');
            }
        });
    }

    // Add 'current' class on initial load
    addCurrentClass();

    // Update 'current' class on hash change
    window.addEventListener('hashchange', addCurrentClass);
});
