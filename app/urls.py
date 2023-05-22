from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from Ecom import views as Ecom_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ecom.urls')),
    path('register_customers/', user_views.register_customer, name='register_customers'),
    path('register_vendors/', user_views.register_vendor, name='register_vendors'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
    path('login_google/', TemplateView.as_view(template_name="googlelogin.html") , name='login'),
]
