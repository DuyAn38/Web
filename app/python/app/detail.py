from django.shortcuts import get_object_or_404, render
from app.models import Cart
from app.models import *


def detail(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    fixed_comment = "100px"
    #check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        for item in items:
            print(item) 
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"
    id = request.GET.get('id', '') # lấy id khi người dùng Click vào sản phẩm nào đó
    user = request.user
    products = get_object_or_404(Product, id=id)
    categories_product = products.category.values_list('id', flat=True)
    # Lấy danh sách tên danh mục từ danh sách ID
    category_names = Category.objects.filter(id__in=categories_product).values_list('name', flat=True)
    print(category_names)
    # Chuyển danh sách tên thành danh sách Python
    category_names_list = list(category_names)
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {
               'category_names_list': category_names_list,
               'products': products,
               'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'fixed_comment': fixed_comment,
               'show_manage': show_manage,
               }
    return render(request, 'app/detail.html', context)
