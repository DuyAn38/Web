from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Slide)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Cart)
# Register your models here.