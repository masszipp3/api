from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index),
    path('customers',views.customer),
    path('product_create',views.productscreate.as_view()),
    path('category_create',views.categorycreate.as_view()),

]