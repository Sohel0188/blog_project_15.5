from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name="musicians"),  
    path('delete_musician/<int:id>/', views.delete, name="delete_musician"),  
    path('edit_musician/<int:id>/', views.edit_musician, name="edit_musician"),  
]