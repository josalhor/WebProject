from django.urls import path
#from .views import hello_world
from apps.hello_world.views import hello_world

urlpatterns = [
    path('hello', hello_world, name='hello_world_name')
]