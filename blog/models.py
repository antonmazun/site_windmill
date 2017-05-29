from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date


class Dish(models.Model):
    BRAND_FOOD = 'фірмові_страви'  # фірмова страва
    SALAD = 'салат'  # cалат
    COLD_SNECK = 'холодна_закуска'  # холодна закуска
    HOT_SNECK = 'гаряча_закуска'  # гаряча
    FIRST_DISH = 'перші_страви'
    SECOND_DISH = 'другі_страви'
    GARNISH = 'гарнір'
    PANCAKES = 'деруни'  # деруни та гречаники
    TEA = 'чай'
    COFFE = 'кава'
    TYPE = (
        (BRAND_FOOD, 'фірмові_страви'),
        (SALAD, 'салат'),
        (COLD_SNECK, 'холодна_закуска'),
        (HOT_SNECK, 'гаряча_закуска'),
        (FIRST_DISH, 'перші_страви'),
        (SECOND_DISH, 'другі_страви'),
        (GARNISH, 'гарнір'),
        (TEA, 'чай'),
        (COFFE, 'кава'),
    )

    name = models.CharField(max_length=10000)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.IntegerField()
    type = ArrayField(models.CharField(max_length=10000, choices=TYPE), size=40, default=None)
   # image = models.ImageField(upload_to='image/', null=True, default='image/images.jpg')

    def __str__(self):
        return self.name

    def dict(self):
        return {'name': self.name,
                'description': self.description,
                'weight': self.weight,
                'price': self.price,
                'types': [i for i in self.type]
                }


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profile'
