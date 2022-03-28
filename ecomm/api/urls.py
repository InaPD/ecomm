from django.urls import path
from . import views

urlpatterns=[
    path('',views.viewProducts),
    path('addProduct/',views.addProduct),
    path('addUser/',views.addUser),
    path('<slug>/delete/',views.deleteItem),
]