document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('dark-mode-toggle');
    console.log('Toggle button:', toggleButton); // Check if the button is captured
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            var icon = document.getElementById('toggle-icon');
            console.log('Current icon classes:', icon.classList); // Log current classes
            if (icon.classList.contains('fa-moon')) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
            console.log('Updated icon classes:', icon.classList); // Log updated classes
        });
    } else {
        console.error('Dark mode toggle button not found');
    }
});
