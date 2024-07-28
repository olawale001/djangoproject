from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('record_sale/', views.record_sale, name='record_sale'),
    path('record_order/', views.record_order, name='record_order'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('inventory/', views.inventory, name='inventory'),
    # path('products/', views.products, name='products'),
]
