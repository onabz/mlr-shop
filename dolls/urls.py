from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dolls, name='dolls'),
    path('<doll_id>', views.doll_detail, name='doll_detail'),
]
