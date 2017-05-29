from django.conf.urls import url , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    #url(r'^$', views.Main),
    url(r'^all/$', views.Dishes),
    url(r'^add_comments/$', views.add_comments),
    url(r'^add/$', views.Add),
    url(r'^add_photo/$', views.addPhoto),
    url(r'^add_news/$', views.add_news),
    url(r'^news/$', views.news),
    url(r'^contacts/$', views.contacts),
    url(r'^gallery/salatove/$', views.salatove, name='main'),
    url(r'^gallery/marsala/$', views.marsala, name='main'),
    url(r'^gallery/rustik/$', views.rustik, name='main'),
    url(r'^gallery/bir/$', views.bir, name='main'),
    url(r'^del/(\d+)/$', views.Delete, name='main'),
    url(r'^del_comments/(\d+)/$', views.del_comments, name='main'),
    url(r'^del_news/(\d+)/$', views.del_news, name='main'),
    url(r'^dishes/(\d+)/$', views.Dishes_id, name = 'main'),
    url(r'^specialty/$', views.Specialty, name = 'main'),
    url(r'^cold_snacks/$', views.Cold_snacks, name = 'main'),
    url(r'^hot_snacks/$', views.Hot_snacks, name = 'main'),
    url(r'^first_courses/$', views.First_courses, name = 'main'),
    url(r'^garnish/$', views.Garnish, name = 'main'),
    url(r'^main_dishes/$', views.Main_dishes, name = 'main'),
    url(r'^vareniki/$', views.Vareniki, name = 'main'),
    url(r'^desserts/$', views.Desserts, name = 'main'),
    url(r'^alcohol/$', views.Alcohol, name = 'main'),
]