from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='bronze')


class Category(models.Model):
    cafget_name = models.CharField(max_length=100)


class Food(models.Model):
    resto_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Courier(models.Model):
    courier_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('car', 'car'),
        ('bike', 'bike'),
        ('walk', 'walk'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)


class Order(models.Model):
    order_number = models.PositiveIntegerField(default=0)
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField(auto_now_add=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('доставлено', 'доставлено'),
        ('В обработке', 'В обработке'),
        ('В пути', 'В пути')
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)


class Rating(models.Model):
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Rating")


class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,  )

