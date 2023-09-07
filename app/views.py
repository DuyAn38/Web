# from itertools import product
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
# app
from .python.app.base import *
from .python.app.information_address import information_address
from .python.app.cart import cart

from .python.app.category import category
from .python.app.check_address import Continue1
from .python.app.checkout import checkout
from .python.app.detail import detail
from .python.app.information import Information
from .python.app.login import loginPage, logoutPage
from .python.app.register import register
from .python.app.search import searchProduct
from .python.app.updateItem import updateItem

from .python.app.manage_address import addAddress, editAddress, deleteAddress
# admin
from .python.admin.manage import Manage
from .python.admin.manage_slide import manageSlide
from .python.admin.manage_user import manageUser
from .python.admin.manage_category import manageCategory, addCategory, editCategory, deleteCategory
from .python.admin.manage_product import manageProduct, addProduct, editProduct, deleteProduct, viewProduct
#API
from .API.products_api import *
from .API.category_api import *


def myOrder(request):
    slide_hidden = "hidden"
    fixed_height = "20px"

    my_orders = Order.objects.filter(customer=request.user)
    order_items = {}  # Tạo một từ điển để lưu trữ các đơn hàng và mặt hàng tương ứng
    order_addresses = {}  # Tạo một từ điển để lưu trữ đơn hàng và thông tin địa chỉ tương ứng
    order_total_amounts = {}

    for order in my_orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order] = items
        total_order_amount = 0
        for item in items:
            total_order_amount += item.total
            print("tong gia order : ")
            print(total_order_amount)
        order_total_amounts[order.id] = total_order_amount
        order_total_amounts_list = [(order.id, total_amount) for order.id, total_amount in order_total_amounts.items()]

        address = order.address  # Truy cập vào đối tượng Address liên kết với đơn hàng
        order_addresses[order] = address
        if order in order_total_amounts:
            print(f"Giá trị đã được lưu cho đơn hàng '{order}': {order_total_amounts[order]}")
        else:
            print(f"Không tìm thấy giá trị cho đơn hàng '{order}' trong order_total_amounts.")


    context = {
        'order_addresses': order_addresses,
        'order_items': order_items,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage,
        'my_order': my_orders,
        'items': items,
        'order_total_amounts': order_total_amounts,
        'total_order_amount': total_order_amount,
        'order_total_amounts_list': order_total_amounts_list,
    }
    return render(request, 'app/my_order.html', context)




