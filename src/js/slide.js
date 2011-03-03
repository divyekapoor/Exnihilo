(function($) {
    $(document).ready(function() {
        // Expand Panel
        $("#open").click(function(){
	        $("div#panel").slideDown("fast");
            return false;
        });

        // Collapse Panel
        $("#close").click(function(){
	        $("div#panel").slideUp("fast");
            return false;
        });

        // Switch buttons from "Log In | Register" to "Close Panel" on click
        $("#toggle a").click(function () {
	        $("#toggle a").toggle();
        });
    });
    
})(jQuery);
