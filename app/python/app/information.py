from django.shortcuts import render

from app.models import *
from app.python.app.base import show_manage
def Information(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated:
        user = request.user
        address_infor = Address.objects.filter(customer=user)
    user_address = None
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            mobile = form.cleaned_data['mobile']
            user_address = Address(customer=request.user, adress=address, city=city, state=state, mobile=mobile)
            user_address.save()
    else:
        form = AddressForm()
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
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"

    context = {'user': user,
               'form': form,
               'address_infor': address_infor,
               'user_address': user_address,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'user_not_login': user_not_login,
               'user_login': user_login,
               'items': items,
               'total_all': total_all,
               'count': count,
               'show_manage': show_manage,
               }
    return render(request, 'app/information.html', context)
