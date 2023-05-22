from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
from django.shortcuts import reverse
from django.core.mail import send_mail

class Post(models.Model):
    item = models.CharField(max_length = 30)
    slug = models.SlugField()
    stock = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='item_pics')
    description = models.CharField(max_length = 30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.CharField(max_length = 100, default = "no reviews yet")
    
    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse("Ecom:product", kwargs={
            'slug': self.slug
        })
        
    def get_add_to_cart_url(self):
        return reverse("Ecom:add-to-cart", kwargs={
            'slug': self.slug
        })
        
    def get_remove_from_cart_url(self):
        return reverse("Ecom:remove-from-cart", kwargs={
            'slug': self.slug
        })
        
    def write_review(self):
        return reverse("Ecom:add review", kwargs={
            'slug': self.slug
        })
     
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item}"

    def get_final_price(self):
        return self.quantity * self.item.price

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    
    send_mail(
        "Notification from Ecom",
        "Order placed",
        "sohanreddy99999@gmail.com",
        ["sohanreddy99999@gmail.com"],
    )
    
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    one_click_purchasing = models.BooleanField(default=False)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    balance=models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
#class write_review(models.Model, slug):
    #reviews=models.CharField(Post,slug = slug) 

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)

post_save.connect(userprofile_receiver, sender=User)