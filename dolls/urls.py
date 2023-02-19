from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dolls, name='dolls'),
    path('<int:doll_id>', views.doll_detail, name='doll_detail'),
    path('add/', views.add_doll, name='add_doll'),
    path('edit/<int:doll_id>/', views.edit_doll, name='edit_doll'),
    path('delete/<int:doll_id>/', views.delete_doll, name='delete_doll'),
]
