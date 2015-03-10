$(document).ready(function() {
    $('div').click(function() {
    	$(this).children('audio').get(0).play();
    });
});

