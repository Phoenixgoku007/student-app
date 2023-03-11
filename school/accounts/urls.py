from django.urls import path, include
from .import views

urlpatterns = [
    #path('',views.home,name='home'),
    path('login/',views.login,name='login'),         
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout_user'),
    path('delete/',views.delete_user,name='delete_user'),
    path('student_login/',views.student_login,name='student_login'),
    path('profile/',views.profile,name='profile'),
]

