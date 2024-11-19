from django.urls import path 
from subscribe_app import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'), 

]

