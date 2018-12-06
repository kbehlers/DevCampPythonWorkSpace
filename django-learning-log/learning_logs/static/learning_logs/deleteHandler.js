window.addEventListener('load', function () {
    var deleteLinks = document.querySelectorAll('.delete-form');

    for (var i = 0; i < deleteLinks.length; i++) {
        deleteLinks[i].addEventListener('submit', function (event) {
            var choice = confirm("\n\nAre you sure you want to PERMANENTLY delete the entry?\n\nPress OK to proceed with deletion\nPress Cancel to go back");

            if (choice) {
                console.log(event)
            }
            else {
                event.preventDefault();
            }
        });
    }
}, false);