from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from location.models import Region
from accounts.models import CustomUser


class Restaurant(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phone_number_1 = models.CharField(max_length=12)
    # phone = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number_2 = models.CharField(max_length=12)
    manager_email_address = models.EmailField(max_length=100)
    manager_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='restaurant')
    restaurant_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Restaurant_Image', upload_to='restaurant/restaurant_img', blank=True, )
    logo = models.ImageField(verbose_name='Restaurant_Logo', upload_to='restaurant/restaurant_logo', blank=True, )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Menu(models.Model):
    food_name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name




