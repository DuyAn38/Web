import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Cart, Product

@login_required
def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data.get('productId')
        action = data.get('action')
        selectedSize = data.get('size')  # Lấy kích cỡ từ dữ liệu yêu cầu

        size = selectedSize
        print('size: ')
        print(size)

        customer = request.user
        product = Product.objects.get(id=productId)

        # Tìm sản phẩm trong giỏ hàng có cùng sản phẩm và kích cỡ
        cart, created = Cart.objects.get_or_create(product=product, user=request.user, size=size)

        if action == 'add':
            cart.quantity += 1
        elif action == 'remove':
            cart.quantity -= 1

        # Kiểm tra nếu số lượng sản phẩm trong giỏ hàng <= 0, thì xóa sản phẩm khỏi giỏ hàng
        if cart.quantity <= 0:
            cart.delete()
        else:
            cart.save()

        return JsonResponse('added', safe=False)
