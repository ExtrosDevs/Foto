var cons = document.getElementById("contacts");


// Get all buttons with class="chat-name" inside the container
var names = cons.getElementsByClassName("chat-name");
var nav = cons.getElementsByClassName("nav-link");


// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < names.length; i++) {
  names[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";

    $(".nav-link").on('click', function(){
    for (var i = 0; i < names.length; i++) {
    current[0].className = current[0].className.replace(" active", "");
        
    }


});
  });
}
