document.addEventListener("DOMContentLoaded", function() {
  // Define the levels you want to make expandable
  var levels = ['toctree-l1', 'toctree-l2', 'toctree-l3'];

  levels.forEach(function(level) {
    // Select all <li> elements with the current level class
    var toctreeItems = document.querySelectorAll('li.' + level);

    toctreeItems.forEach(function(item) {
      // Find the link within the item
      var link = item.querySelector('a');
      var nestedList = item.querySelector('ul');

      if (link && nestedList) {
        // Create a wrapper span for the text and icon
        var wrapper = document.createElement('span');
        wrapper.className = 'no-break-chevron';

        // Move the link text into the wrapper
        var linkText = document.createTextNode(link.textContent);
        wrapper.appendChild(linkText);
        link.textContent = '';
        link.appendChild(wrapper);

        var expandSign = document.createElement('img');
        expandSign.className = 'chevron-icon';
        expandSign.style.width = '12px';
        expandSign.style.height = '12px';
        expandSign.style.marginLeft = '5px';
        expandSign.style.cursor = 'pointer';

        // Append the icon to the wrapper
        wrapper.appendChild(expandSign);

        // Use the link text and level as a unique key for localStorage
        var sectionKey = level + '_section_' + link.textContent.trim().replace(/\s+/g, '_');

        // Retrieve the saved state from localStorage
        var isExpanded = localStorage.getItem(sectionKey);

        // If no state is saved, default to expanded for "Learn the Basics" and collapsed for others
        if (isExpanded === null) {
          isExpanded = (link.textContent.trim() === 'Learn the Basics') ? 'true' : 'false';
          localStorage.setItem(sectionKey, isExpanded);
        }

        // Set the initial display state based on the saved or default state
        if (isExpanded === 'true') {
          nestedList.style.display = 'block'; // Expand the section
          expandSign.src = chevronDownIconPath; // Use the down chevron icon
        } else {
          nestedList.style.display = 'none'; // Collapse the section
          expandSign.src = chevronRightIconPath; // Use the right chevron icon
        }

        // Add a click event to toggle the nested list
        expandSign.addEventListener('click', function() {
          if (nestedList.style.display === 'none') {
            nestedList.style.display = 'block';
            expandSign.src = chevronDownIconPath; // Change to down chevron when expanded
            localStorage.setItem(sectionKey, 'true'); // Save state
          } else {
            nestedList.style.display = 'none';
            expandSign.src = chevronRightIconPath; // Change back to right chevron when collapsed
            localStorage.setItem(sectionKey, 'false'); // Save state
          }
        });
      }
    });
  });
});
