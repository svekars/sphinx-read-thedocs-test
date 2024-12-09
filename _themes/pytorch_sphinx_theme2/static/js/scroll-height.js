document.addEventListener("DOMContentLoaded", function() {
    // Check if the current page URL contains 'generated/'
    if (window.location.href.includes('generated/')) {
        const offset = 400; // Offset in pixels

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault(); // Prevent default anchor click behavior

                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);

                if (targetElement) {
                    // Scroll to the element with the specified offset
                    window.scrollTo({
                        top: targetElement.offsetTop - offset,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
});
