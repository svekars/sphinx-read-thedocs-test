$(document).ready(function() {
  // Event listener for click on toggle-icon
  $('.toggle-icon').click(function() {
    var $this = $(this);
    var $parentLi = $this.closest('li');

    // Toggle the 'expanded' class on the li element
    $parentLi.toggleClass('expanded');

    // Find the next ul element (which should be your sub-menu) and toggle its visibility
    $parentLi.find('> ul').slideToggle();

    // Update the background image based on the expanded state
    if ($parentLi.hasClass('expanded')) {
      $this.css('background-image', 'url("../images/chevron-up-black.svg")');
    } else {
      $this.css('background-image', 'url("../images/chevron-down-black.svg")');
    }
  });
});
