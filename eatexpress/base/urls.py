from django.urls import path
# from .views import OrderListView
from . import views
from users import views as user_views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('api/dishes/', views.get_dishes, name='get_dishes'),
    path('services/', views.services, name='services'),
]