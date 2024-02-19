from django.urls import path
from app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.detail, name='detial'),
    path('create_product/',views.create_product, name='create_product'),
    path('update/<int:id>/',views.update_product, name='update_product'),
    path('delete/<int:id>/',views.delete_product, name='delete_product'),
]