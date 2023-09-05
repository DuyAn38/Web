var updateBtns = document.getElementsByClassName('update-btn');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        
        var radioButtons = document.querySelectorAll('input[type="radio"][name="optionsRadios"]');
        var selectedSize = null;

        radioButtons.forEach(function (radio) {
            if (radio.checked) {
                selectedSize = radio.value;
            }
        });

        console.log(productId);
        console.log('action: ', action);
        console.log('user: ', user);
        console.log('selectedSize: ', selectedSize);

        if (user === "AnonymousUser") {
            console.log("User not logged in");
        } else {
            updateUserOrder(productId, action, selectedSize);
        }
    });
}

function updateUserOrder(productId, action, selectedSize) {
    console.log("User logged in");
    console.log("id: ", productId);
    console.log("action: ", action);
    console.log("selectedSize: ", selectedSize);

    var url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action, 'size': selectedSize })
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log('data: ', data);
        location.reload();
    });
}
