import json

from django.http import JsonResponse

from app.models import *


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    selectedSize = data.get('size', None)  # Lấy kích cỡ từ dữ liệu yêu cầu
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, size=selectedSize)  # Lưu kích cỡ vào OrderItem

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('added', safe=False)

