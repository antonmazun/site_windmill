from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone



class Dish(models.Model):

    BRAND_FOOD = 'фірмові страви' # фірмова страва
    SALAD  = 'салат' #cалат
    COLD_SNECK = 'холодні закуски' # холодна закуска
    HOT_SNECK = 'гарячі закуски' #гаряча
    FIRST_DISH = 'перші страви'
    SECOND_DISH = 'другі страви'
    GARNISH = 'гарніри'
    PANCAKES = 'деруни' # деруни та гречаники
    DESSERTS = 'десерти'
    TEA = 'чай'
    COFFE = 'кава'
    AlCOHOL = 'алкоголь'
    TYPE = (
        (BRAND_FOOD , 'фірмові страви'),
        (SALAD , 'салат'),
        (COLD_SNECK , 'холодні закуски'),
        (HOT_SNECK , 'гарячі закуски'),
        (FIRST_DISH , 'перші страви'),
        (SECOND_DISH , 'другі страви'),
        (GARNISH , 'гарніри'),
        (PANCAKES, 'деруни'),
        (DESSERTS, 'десерти'),
        (AlCOHOL, 'алкоголь'),
        (TEA , 'чай'),
        (COFFE , 'кава'),
    )

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=100000)
    weight = models.IntegerField()
    price  = models.IntegerField()
    type = models.CharField(max_length=30, choices=TYPE)
   # image = models.ImageField(upload_to='image/', null=True, default='media/image/images.jpg')
    #type = ArrayField(models.CharField(max_length=150, choices=TYPE), size=40 ,default=None)

    def __str__(self):
        return self.name

    def dict(self):
        return {'name' : self.name ,
                'description' : self.description,
                'weight' : self.weight,
                'price' : self.price,
                'types' : [i for i in self.type]
                }

class Novosti(models.Model):
    content1 = models.CharField(max_length=100000)
    img1 = models.ImageField(upload_to='image/', null=True)
    title1 = models.CharField(max_length=100)

    def __str__(self):
        return self.content1

    def dict(self):
        return {
            'content': self.content1,
            'title': self.title1,
        }


class Photo(models.Model):
    SALATOVE = 'салатове'  # фірмова страва
    MARSALA = 'марсала'  # cалат
    RUSTIK = 'рустік'  # холодна закуска
    BIR = 'бірьозове'

    TYPE = (
        (SALATOVE , 'салатове'),
        (MARSALA , 'марсала'),
        (RUSTIK , 'рустік'),
        (BIR , 'бірьозове'),
    )



    photo = models.ImageField(upload_to='image/' , null=True)
    type_photo = models.CharField(max_length=30, choices=TYPE ,default='салатове')

    def __str__(self):
        return self.type_photo

    def dict(self):
        return {
            'photo': self.photo,
        }

class Comments(models.Model):

    text = models.TextField(max_length=500)
    author_name = models.TextField(max_length=100, default="Анонім")

    def dict(self):
        return {
            'text': self.text,
            "author_name": self.author_name,
        }
