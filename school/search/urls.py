from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('get-names/',views.get_names,name='get_names'),
]
