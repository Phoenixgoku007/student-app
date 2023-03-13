from django.urls import path
from .import views

urlpatterns = [
    # other URL patterns here...
    path('add/', views.add_user_view, name='add_user_view'),
    path('search/', views.search_view, name='search_view'),
    path('display/',views.student_list, name='student_list'),
]

