from django.shortcuts import get_object_or_404, render
from app.models import *

def detail(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    fixed_comment = "100px"

    # Check xem phải admin không
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

    form = CommentForm()
    id = request.GET.get('id', '') # Lấy id khi người dùng click vào sản phẩm nào đó
    user = request.user
    products = get_object_or_404(Product, id=id)
    comment = Comment.objects.filter(product=products) # Lấy đúng cái cmt của cái sp đó

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['title']
            comments = Comment(user=user, product=products, title=content)
            comments.save()

    # Lấy danh sách id danh mục từ request.GET
    category_ids = request.GET.getlist('categories_product')

    # Lấy danh sách tên danh mục từ cơ sở dữ liệu
    category_names = Category.objects.filter(id__in=category_ids).values_list('name', flat=True)

    # Chuyển danh sách tên thành danh sách Python
    category_name_list = list(category_names)

    # Lấy các danh mục lớn
    categories = Category.objects.filter(is_sub=False)

    context = {
        'form': form,
        'comments': comment,
        'products': products,
        'category_name_list': category_name_list,
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
