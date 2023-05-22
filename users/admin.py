from django.contrib import admin
from .models  import vendor_profile, previousorders

# Register your models here.

admin.site.register(vendor_profile)
admin.site.register(previousorders)
