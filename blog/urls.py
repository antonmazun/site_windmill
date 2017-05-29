from django.conf.urls import url , include
from django.contrib import admin
from . import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = [

    url(r'^contact/$', views.contactform, name='contact'),
    url(r'^about_us/$', views.about_us, name='contact'),
    url(r'^gallery/$', views.gallery, name = 'main'),
    url(r'^news/$' , views.news),
    # url(r'^thanks/$' , views.thanks , name = 'thanks'),
    # url(r'^sign_up/', views.register_user),
   # url(r'^register_success/', views.registere_success),
    #url(r'^confirm/(?P\w+)/', views.register_confirm),
    url(r'^$', views.show),

]