from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Product List"),
    path('<int:product_id>',views.detail,name="Product Detail"),
    path('create',views.create)

]