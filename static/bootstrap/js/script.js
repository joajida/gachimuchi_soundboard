$(document).ready(function() {
    $('div').click(function() {
    	$(this).children('audio').get(0).play();
    	$(this).children('div').toggleClass('box_rotate');
    });
});

