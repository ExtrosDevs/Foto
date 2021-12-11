//blur the ful image 
$("#im").click(function () {
    $(".full").toggle();
    $("body").css({
        filter: "blur(2px)"
    });
});
$(".full").click(function () {
    $(".full").toggle();
    $("body").css({
        filter: "blur(0px)"
    });
});
//blue the mini image
$("#im").css({
    filter: "blur(2px)"
});
//prevent from right click
document.addEventListener('contextmenu', event => event.preventDefault());
//prevent from dragging the image 
$(document).ready(function () {
    $('#full').on('dragstart', function () {
        return false;
    });
    $('#im').on('dragstart', function () {
        return false;
    });
});
//prevent from download
$('#download-link').css("pointer-events", "none");

//prevent ctrl+shift
document.onkeydown = function(e) {
    if(event.keyCode == 123) {
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'E'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'S'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'H'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'A'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'F'.charCodeAt(0)){
    return false;
    }
    if(e.ctrlKey && e.keyCode == 'E'.charCodeAt(0)){
    return false;
    }
    }

    