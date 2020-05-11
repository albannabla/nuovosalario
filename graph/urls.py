from django.urls import path
from . import views
from .views import ShopList, avg

urlpatterns = [
    path('', ShopList.as_view()),
    path('average', avg.as_view()),
    path('update', views.index),
]
