document.addEventListener("DOMContentLoaded", function() {
    const dropdownToggle = document.querySelector('.custom-version-dropdown .dropdown-toggle');
    const dropdownMenu = document.querySelector('.custom-version-dropdown .dropdown-menu');

    // Fetch and populate dropdown menu with versions
    fetch('https://raw.githubusercontent.com/pytorch/docs/refs/heads/site/versions.html')
      .then(response => response.text())
      .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, 'text/html');
        const versionList = doc.querySelectorAll('.toctree-l1 a');
        let defaultVersionSet = false;

        versionList.forEach(version => {
          const li = document.createElement('li');
          li.textContent = version.textContent;
          li.addEventListener('click', function() {
            dropdownToggle.textContent = version.textContent;
            dropdownMenu.style.display = 'none';
          });
          dropdownMenu.appendChild(li);

          // Set the default version if it contains "(stable)"
          if (!defaultVersionSet && version.textContent.includes('(stable)')) {
            dropdownToggle.textContent = version.textContent;
            li.style.fontWeight = 'bold'; // Optional: Highlight the default version
            defaultVersionSet = true;
          }
        });

        // If no stable version is found, set the first version as default
        if (!defaultVersionSet && versionList.length > 0) {
          dropdownToggle.textContent = versionList[0].textContent;
        }
      })
      .catch(error => console.error('Error fetching version.html:', error));

    dropdownToggle.addEventListener('click', function() {
      dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    document.addEventListener('click', function(event) {
      if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none';
      }
    });
});
