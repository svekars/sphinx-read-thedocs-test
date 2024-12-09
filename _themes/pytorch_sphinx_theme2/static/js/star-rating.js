document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.fa-star');
    let selectedRating = 0; // Variable to store the selected rating

    stars.forEach(star => {
        star.addEventListener('mouseover', handleMouseOver);
        star.addEventListener('mouseout', handleMouseOut);
        star.addEventListener('click', handleClick);
    });

    function handleMouseOver(e) {
        fillStars(e.target.dataset.count);
    }

    function handleMouseOut(e) {
        // Only clear stars if no rating has been selected
        if (selectedRating === 0) {
            clearStars();
        } else {
            fillStars(selectedRating); // Fill stars up to the selected rating
        }
    }

    function handleClick(e) {
        selectedRating = e.target.dataset.count; // Update the selected rating
        console.log('Rated:', selectedRating);
        fillStars(selectedRating); // Keep the stars filled after clicking
    }

    function fillStars(count) {
        clearStars();
        stars.forEach(star => {
            if (star.dataset.count <= count) {
                star.classList.add('star-fill'); 
                star.classList.remove('fa-regular');
                star.classList.add('fas');
            }
        });
    }

    function clearStars() {
        stars.forEach(star => {
            star.classList.remove('star-fill'); 
            star.classList.add('fa-regular');
            star.classList.remove('fas');
        });
    }
});
