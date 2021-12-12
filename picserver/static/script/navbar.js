        $("#search-btn").click(function () {
            $("#search").slideToggle("", function () {

            });
        });
        $("#about-btn").click(function () {
            $(".overlay").fadeToggle("", function () {});
            $(".overlay-content").fadeToggle("", function () {});
            document.getElementById("overlay-p").innerHTML =
                "We are a photo hosting site, that offers a lot of free and premium photo lineup";
        });
        $("#contact-btn").click(function () {
            $(".overlay").fadeToggle("", function () {});
            $(".overlay-content").fadeToggle("", function () {});
            document.getElementById("overlay-p").innerHTML = "Email: ExtrosDevs@gmail.com <br> <br> Github: github.com/ExtrosDevs";
        });
        $("#close-btn").click(function () {
            $(".overlay").fadeToggle("", function () {});
            $(".overlay-content").fadeToggle("", function () {});
        });
        $("#mobile-btn").click(function () {
            $("#login-nav").slideToggle("", function () {});
            $("#contact-btn").slideToggle("", function () {});
            $("#search-btn").slideToggle("", function () {});
            $("#about-btn").slideToggle("", function () {});
            $("#mobile-links").slideToggle("", function () {});
            $(this).text($(this).text() == 'Expand Menu' ? 'Shrink Menu' : 'Expand Menu');

        });


        if ($(window).width() <= 600) {
            $('#contact-btn').hide();
            $('#about-btn').hide();
            $('#search-btn').hide();
            $('#mobile-links').hide();
            $('#login-nav').hide();
        }
        if ($(window).width() > 600) {
            $('#mobile-btn').hide();
            $('#mobile-links').hide();
        }

        $(window).scroll(function () {
            if ($(this).scrollTop()) {
                $('#totop').fadeIn();
            } else {
                $('#totop').fadeOut();
            }
        });

        $("#totop").click(function () {
            $("html, body").animate({
                scrollTop: 0
            }, 500);
        });



        $(document).ready(function () {
            $('#search').hide();
            $('.overlay-content').hide();
    
        });