from django.urls import path
from . import views
from .views import ShopList

urlpatterns = [
    path('', ShopList.as_view()),
    path('update', views.index),
]
