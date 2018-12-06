window.addEventListener('load', function () {
    var deleteLinks = document.querySelectorAll('.btn');

    for (var i = 0; i < deleteLinks.length; i++) {
        deleteLinks[i].addEventListener('click', function (event) {
            event.preventDefault();

            var choice = confirm("Delete?");

            if (choice) {
                console.log("Yikes")
            }
        });
    }
}, false);