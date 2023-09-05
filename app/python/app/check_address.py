from django.contrib import messages
from django.shortcuts import render
from app.models import *

def Continue1(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    
    total_all = 0
    count = 0
    order = None  # Đảm bảo rằng biến order được định nghĩa
    shipping = None  # Đảm bảo rằng biến shipping được định nghĩa
    allAddress = None  # Đảm bảo rằng biến allAddress được định nghĩa

    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
        
        # Tạo các đối tượng OrderItem và liên kết chúng với đơn hàng
        for item in items:
            items_order = OrderItem(product=item.product, order=order, quantity=item.quantity, total=item.product.price * item.quantity)
            items_order.save()
        items.delete()
        
        # Gán giá trị cho biến shipping và allAddress
        shipping = "Thông tin vận chuyển"  
        allAddress = Address.objects.all()

        order = Order(customer=customer, complete=False, address=None)  # Đảm bảo rằng biến order đã được định nghĩa

        for item in items:
            items_order = OrderItem(product=item.product, order=order, quantity=item.quantity)
            items_order.save()
            print("Lưu thành công đối tượng OrderItem")
        products = OrderItem.objects.filter(order=order)
        for item in products:
            item.total = item.product.price * item.quantity
        items.delete()
    else:
        items = []
        user_not_login = "show"
        user_login = "none"

    id = request.GET.get('id', '')
    print("lấy id của address: " + id)
    address = Address.objects.filter(id=id)
    address_data = address.values()
    try:
        single_address = address.get()
        city = single_address.city
        address_sate = single_address.adress
        name = single_address.name_user
        mobile = single_address.mobile
        district = single_address.district
        commune = single_address.commune
        
        order = Order(customer=customer, address=single_address, complete=False)
        order.save()

        for item in items:
            items_order = OrderItem(product=item.product, order=order, quantity=item.quantity)
            items_order.save()
            print("Lưu thành công đối tượng OrderItem")
    except Address.DoesNotExist:
        pass
    print(name, city, address_sate, mobile, district, commune)
    for item in items:
        print(item)
    
    context = {
        'shipping': shipping,
        'products': Product.objects.all(),  # Thay 'Product' bằng tên thực của model nếu cần
        'total_all': total_all,
        'count': count,
        'user_login': user_login,
        'user_not_login': user_not_login,
        'allAddress': allAddress,
        'messages': messages,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage
    }
    
    return render(request, 'app/address.html', context)
