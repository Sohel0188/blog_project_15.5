from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name="album"),   
    path('edit_album/<int:id>', views.edit, name="edit_album"),   
]