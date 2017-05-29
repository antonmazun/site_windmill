from django.contrib import admin
from .models import Dish , Novosti , Photo , Comments
# Register your models here.

admin.site.register(Dish)
admin.site.register(Novosti)
admin.site.register(Photo)
admin.site.register(Comments)