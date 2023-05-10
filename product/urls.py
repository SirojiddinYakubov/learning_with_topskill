from django.urls import path

from product import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<int:product_id>/', views.products_detail, name='product_detail'),
    path('about/', views.about, name='about'),
]
