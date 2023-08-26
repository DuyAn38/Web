var updateBtns = document.getElementsByClassName('update-btn')
for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log(productId);
        console.log('action: ', action);
        console.log('user: ', user)
        if (user === "AnonymousUser") {
            console.log("User not login");
        } else {
            updateUserOrder(productId, action);
        }
    })
}

function updateUserOrder(productId, action){
    console.log("User login ok");
    console.log("id: ", productId);
    console.log("action 2: ", action);
    var url = '/update_item/';
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    }).then((reponse) =>{
       return reponse.json();
       
    }).then((data) =>{
        console.log('data: ', data)
        location.reload();
    })
}


document.addEventListener("DOMContentLoaded", function () {
    // Lắng nghe sự kiện khi người dùng ấn nút "Thêm vào giỏ hàng"
    var addToCartButton = document.querySelector(".add-btn");
    addToCartButton.addEventListener("click", function () {
        // Lấy giá trị của kích cỡ đã chọn
        var selectedSize = document.querySelector("input[name='optionsRadios']:checked").value;

        // Sử dụng selectedSize để thêm vào giỏ hàng (đây là nơi bạn xử lý logic thêm vào giỏ hàng)
        addToCart(selectedSize);
    });

    // Hàm xử lý logic thêm vào giỏ hàng
    function addToCart(size) {
        // Gửi yêu cầu AJAX hoặc chuyển đến trang xử lý để lưu sản phẩm và kích cỡ vào giỏ hàng
        // Ví dụ sử dụng AJAX để gửi dữ liệu đến máy chủ Django:
        $.ajax({
            url: '/add_to_cart/', // Điều này cần phải được thay đổi thành URL xử lý thêm vào giỏ hàng của bạn
            method: 'POST',
            data: {
                'size': size,
                'product_id': '{{ products.id }}', // Sử dụng template tag để lấy ID sản phẩm
                'csrfmiddlewaretoken': '{{ csrf_token }}', // Sử dụng template tag để lấy CSRF token
            },
            success: function (response) {
                // Xử lý phản hồi từ máy chủ sau khi thêm vào giỏ hàng thành công
                // Ví dụ: hiển thị thông báo, cập nhật giỏ hàng trên giao diện người dùng, v.v.
            },
            error: function (error) {
                // Xử lý lỗi nếu có
            }
        });
    }
});

