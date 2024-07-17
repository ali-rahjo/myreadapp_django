# we need the path 
from django.urls import path
from . import views

# Django recognizes path urls when there are 
# define in the varialbe 'urlpattern'.
app_name  = 'myread-urls'
urlpatterns = [
    path('', views.Home_page, name='home-page')
]