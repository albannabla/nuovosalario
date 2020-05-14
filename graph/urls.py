from django.urls import path
from . import views
from .views import ShopList, avg, Graph

urlpatterns = [
    path('allads', ShopList.as_view()),
    path('average', avg.as_view()),
    path('', Graph.as_view()),
    path('update', views.index),
]
