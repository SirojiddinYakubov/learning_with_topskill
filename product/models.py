from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(verbose_name="Tovar nomi", max_length=50)
    description = models.TextField(verbose_name="Tovar haqida")
    price = models.DecimalField(verbose_name="Narxi", decimal_places=2, max_digits=12)
    discount_percent = models.SmallIntegerField()
    is_active = models.BooleanField(verbose_name="Holati", default=False)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField()
    count = models.IntegerField()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
