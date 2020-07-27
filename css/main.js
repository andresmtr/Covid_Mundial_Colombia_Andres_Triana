var $j = jQuery.noConflict();


$j(document).ready(function() {
    var is_open = 0,
        clickEventType = ((document.ontouchstart !== null) ? 'mouseup' : 'touchstart');
   

    function close_nav() {
        $j('html').removeClass('nav-js');
        is_open = 0;
       
    }

    function open_nav() {
        
        $j('html').addClass('nav-js');
        is_open = 1;
    }

    $j(document).on(clickEventType, function(e) {
        if (is_open === 1) { // si está abierto

            if (!$j(e.target).closest("#main-navigation").length > 0) { //y no pincho en navegación
                close_nav(); //ciérrate
            }
        } else { // si está cerrado
            if ($j(e.target).closest("#nav-open").length > 0) { //y pincho en nav open
                open_nav(); //abro
            }
        }
    });

    
});