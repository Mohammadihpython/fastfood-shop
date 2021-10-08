from . import views
from django.urls import path

app_name = 'fastfood'
urlpatterns = [
    path('', views.food_list, name='food_list'),
    # path('', views.menu, name='menu'),
    # path('', views.contant, name='about'),

]
