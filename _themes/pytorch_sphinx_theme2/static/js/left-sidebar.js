document.addEventListener('DOMContentLoaded', function() {
    const captions = document.querySelectorAll('.toctree-wrapper .caption');
    const toctreeL1Items = document.querySelectorAll('.toctree-l1 > a');

    function addChevronAndToggle(item, nextElement) {
        const chevronImg = document.createElement('img');
        chevronImg.className = 'chevron-icon';
        chevronImg.src = chevronRightIconPath; // Ensure this path is correctly defined
        chevronImg.style.cursor = 'pointer';
        chevronImg.style.display = 'inline';
        chevronImg.style.width = '12px';
        chevronImg.style.height = '12px';
        chevronImg.style.marginLeft = '4px';
        item.appendChild(chevronImg);
        chevronImg.addEventListener('click', function(event) {
            event.stopImmediatePropagation();
            toggleSubmenu(nextElement, chevronImg);
        });
        if (!item.closest('.current')) {
            nextElement.style.display = 'none';
        }
    }

    function toggleSubmenu(nextElement, chevronImg) {
        const isVisible = nextElement.style.display !== 'none';
        setSubmenuVisibility(nextElement, !isVisible);
        chevronImg.src = isVisible ? chevronRightIconPath : chevronDownIconPath;
    }

    function setSubmenuVisibility(element, isVisible) {
        element.style.display = isVisible ? 'block' : 'none';
        if (isVisible) {
            const subMenus = element.querySelectorAll('ul');
            subMenus.forEach(subMenu => {
                subMenu.style.display = 'block';
                const chevron = subMenu.previousElementSibling.querySelector('.chevron-icon');
                if (chevron) {
                    chevron.src = chevronDownIconPath;
                }
            });
        }
    }

    captions.forEach(caption => {
        const nextElement = caption.nextElementSibling;
        if (nextElement && nextElement.matches('ul')) {
            addChevronAndToggle(caption, nextElement);
        }
    });

    toctreeL1Items.forEach(item => {
        const subUl = link.nextElementSibling;
        if (subUl && subUl.tagName === 'UL') {
            addChevronAndToggle(link, subUl);
        }
    });

    const currentItems = document.querySelectorAll('.toctree-wrapper .current');
    currentItems.forEach(currentItem => {
        let parent = currentItem.parentElement;
        while (parent && !parent.classList.contains('toctree-wrapper')) {
            if (parent.tagName === 'UL' || parent.tagName === 'LI') {
                parent.style.display = 'block';
                if (parent.previousElementSibling && parent.previousElementSibling.querySelector('.chevron-icon')) {
                    parent.previousElementSibling.querySelector('.chevron-icon').src = chevronDownIconPath;
                }
            }
            parent = parent.parentElement;
        }
    });
});


