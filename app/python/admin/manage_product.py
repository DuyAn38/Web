from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def manageProduct(request):
    products = Product.objects.all()
    form = AddProduct()
    context = {'products': products}
    return render(request, 'admin/managementProduct.html', context)

    

def addProduct(request):
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Thông báo thành công và chuyển hướng
            messages.success(request, 'Product saved successfully!')
            return redirect('manageProduct')
        else:
            # Xử lý trường hợp form không hợp lệ
            print(form.errors.as_data())
            print(form.errors)
            count = 0  # Hoặc giá trị mặc định khác tùy ý
    else:
        form = AddProduct()
        count = 0  # Hoặc giá trị mặc định khác tùy ý

    context = {'form': form, 'messages': messages, 'count': count}
    return render(request, 'admin/addProduct.html', context)



def editProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('manageProduct')
    form = AddProduct(instance=product,
                      initial={'name': product.name,
                               'category': product.category.values_list('id', flat=True),
                               'price': product.price,
                               'describe': product.describe,
                               'image': product.image})

    context = {'product': product,
               'form': form}
    return render(request, 'admin/editProduct.html', context)

def deleteProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('manageProduct')
    context ={'product': product}
    return render(request, 'admin/deleteProduct.html', context)

def viewProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    user = request.user
    print(user)
    product = get_object_or_404(Product, id=id)
    count = product.count39 + product.count40 + product.count41
    context = {'product': product,
               'count': count,}
    return render(request, 'admin/view_product.html', context)