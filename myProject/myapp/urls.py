from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'), #empty means main url
    path('counter/',views.counter,name='counter'), # / is required to show that it is the targeted page
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('post/<str:pk>',views.post,name='post') # dynamic url binding, str is the type, pk is the var name
]
