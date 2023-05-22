from django.contrib import admin
from .models import Post,OrderItem,UserProfile,Address,Order,Payment

# Register your models here.

admin.site.register(Post)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Address)
admin.site.register(UserProfile)
