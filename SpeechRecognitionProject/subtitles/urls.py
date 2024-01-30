from django.urls import path
from .views import index, get_subtitle

urlpatterns = [
    path('', index, name='index'),
    path('get_subtitle/', get_subtitle, name='get_subtitle'),
]
