from django.urls import path
from . import views
from .views import ShopList, avg, Graph

urlpatterns = [
    path('', ShopList.as_view()),
    path('average', avg.as_view()),
    path('graph', Graph.as_view()),
    path('update', views.index),
]
