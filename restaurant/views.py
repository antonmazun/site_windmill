import json

from django.shortcuts import render, redirect, HttpResponse
from .models import Dish, Novosti, Photo, Comments
from django.http import HttpResponseRedirect


# Create your views here.


# def Main(request):
#     if request.method == "GET":
#         return render(request,"main1.html"  , {})

def Dishes(request):
    if request.method == "GET":
        return render(request, "dish.html", {'dishes': Dish.objects.all()})


def Specialty(request):
    if request.method == "GET":
        return render(request, "specialty.html", {'dishes': Dish.objects.all()})


def Cold_snacks(request):
    if request.method == "GET":
        return render(request, "cold_snacks.html", {'dishes': Dish.objects.all()})


def Hot_snacks(request):
    if request.method == "GET":
        return render(request, "hot_snacks.html", {'dishes': Dish.objects.all()})


def First_courses(request):
    if request.method == "GET":
        return render(request, "first_courses.html", {'dishes': Dish.objects.all()})


def Garnish(request):
    if request.method == "GET":
        return render(request, "garnish.html", {'dishes': Dish.objects.all()})


def Main_dishes(request):
    if request.method == "GET":
        return render(request, "main_dishes.html", {'dishes': Dish.objects.all()})


def Vareniki(request):
    if request.method == "GET":
        return render(request, "vareniki.html", {'dishes': Dish.objects.all()})


def Desserts(request):
    if request.method == "GET":
        return render(request, "desserts.html", {'dishes': Dish.objects.all()})


def Alcohol(request):
    if request.method == "GET":
        return render(request, "alcohol.html", {'dishes': Dish.objects.all()})


def salatove(request):
    if request.method == "GET":
        return render(request, "salatove.html", {'salatove': Photo.objects.all()})

def marsala(request):
    if request.method == "GET":
        return render(request, "marsala.html", {'marsala': Photo.objects.all()})

def rustik(request):
    if request.method == "GET":
        return render(request, "rustik.html", {'rustik': Photo.objects.all()})

def bir(request):
    if request.method == "GET":
        return render(request, "bir.html", {'bir': Photo.objects.all()})

def Add(request):
    result = "Страва успішно додана!"
    error = "Ви не адмін!"
    if request.user.is_superuser:
        if request.method == "POST" and request.POST['name'] and request.POST['description'] and request.POST[
            'weight'] and request.POST['price'] and request.POST['select']:
            # form = Restaurants_Form(request.POST, request.FILES)
            Dish.objects.create(name=request.POST['name'],
                                description=request.POST['description'],
                                weight=request.POST['weight'],
                                price=request.POST['price'],
                                type=request.POST['select'])
            return render(request, "home.html", {'result': result})
        elif request.method == "GET":

            return render(request, "add.html", {})
        return HttpResponse('NE POST')
    return render(request, "home.html", {'error': error})


def addPhoto(request):
    result = "Фото успішно додано!"
    if request.user.is_superuser:
        if request.method == "POST" and request.POST['select_photo'] and request.FILES['photo']:
            Photo.objects.create(photo=request.FILES['photo'],
                                 type_photo=request.POST['select_photo']
                                 )
            return redirect("/gallery", {'result': result})
        return redirect('/')
    return HttpResponse("Не работает")


def add_news(request):
    res = "Новина успішно опублікована!"
    if request.user.is_superuser:
        if request.POST and request.POST['content1'] and request.FILES['img1'] and request.POST['title1']:
            Novosti.objects.create(content1=request.POST['content1'],
                                   img1=request.FILES['img1'],
                                   title1=request.POST['title1'])
            return redirect("/news", {'result': res})
        else:
            if request.method == "GET":
                return redirect("/news", {'novosti': Novosti.objects.all()})
    else:
        return render(request, "main1.html", {})


def news(request):
    if request.method == "GET":
        return render(request, "news.html", {'news': Novosti.objects.all()})


def Delete(request, id):
    result = "Видалення пройшло успішно!"
    if request.method == "POST" and request.user.is_superuser:
        Dish.objects.get(id=int(id)).delete()
        return render( request , "home.html", {'result': result})
    elif request.method == "GET":
        return redirect('/')


def del_news(request, id):
    result = "Новина успішно видалена!"
    if request.method == "POST" and request.user.is_superuser:
        Novosti.objects.get(id=int(id)).delete()
        return redirect("/", {'result': result})
    else:
        return redirect('/')

def del_comments(request , id):
    result = "Коментар успішно видалений!"
    if request.method == "POST" and request.user.is_superuser:
        Comments.objects.get(id = int(id)).delete()
        return redirect("/about_us" , {'result' : result})
    elif request.method == "GET" :
        return redirect('/')

def Dishes_id(request, id):
    if request.method == "GET":
        return render(request, "dish.html", {'dishes': [Dish.objects.get(id=int(id))]})

def contacts(request):
    if request.method == "GET":
        return render(request , "contacts.html" , {})


def add_comments(request):
    result = 'Дякуємо , що залишили відгук. Це дуже важливо для нас!'
    if request.method == "POST" and request.POST['text'] or request.POST['author_name']:
        if request.POST['author_name'] == None:
            default_auth_name = 'Анонім'
            Comments.objects.create(
                text = request.POST['text'],
                author_name = request.POST[default_auth_name]
            )
        elif request.POST['author_name'] != None :
            Comments.objects.create(
                text=request.POST['text'],
                author_name=request.POST['author_name']
            )
        # return HttpResponse(json.dumps({"comments": [i.dict() for i in Comments.objects.all()]}), content_type="application/javascript")

        return render(request , "about_us.html" , {'comments' : Comments.objects.all() , 'result':result})
    return render(request , "about_us.html" , {'comments' : Comments.objects.all() , 'result':result})


'''


    elif request.method == 'POST' and request.POST['text'] and request.user.is_authenticated():
        error = False
        if request.session.get('has_commented_already', False):
            error = "You have already commented this post!"
        else:
            Comments.objects.create(comments = request.POST['text'] , creator = request.user , phone = Phone.objects.get(id = int(path)))
            request.session['has_commented_already'] = True



 elif request.method == 'POST' and request.POST['text'] and request.user.is_authenticated():
        error = False
        if request.session.get('has_commented_already', False):
            error = "You have already commented this post!"
'''
