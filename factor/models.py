from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant
from restaurant.models import Menu


class FactorHeader(models.Model):
    title = models.CharField(max_length=200)
    create_datetime = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    factor_header_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FactorBody(models.Model):
    count = models.PositiveIntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    factor_header = models.ForeignKey(FactorHeader, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.count
