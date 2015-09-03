$(window).load(function() {
  // init Masonry
  $.endlessPaginate({
        paginateOnScroll: true,
        paginateOnScrollMargin: 20,
        onCompleted: function(){
        	$('.stock').masonry('reloadItems');   
      		$('.stock').masonry('layout');
        }
    });

  imagesLoaded( document.querySelector('.stock'), function( instance ) {
	  $('.stock').masonry({
	    itemSelector: '.bagi',
	    percentPosition: true,
	    columnWidth: '.grid-sizer'
	  });

	  

	});
  // layout Isotope after each image loads
});