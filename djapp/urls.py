from django.urls import path
from .import views

urlpatterns = [
     path("",views.home,name='home'),
     path('signup/', views.signup, name='signup'),
     path('confirm-email/',views.sentemail, name='confirm-email'),
     path('success',views.success,name='success'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
    
]

