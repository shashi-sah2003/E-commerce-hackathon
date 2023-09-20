from django.urls import path
from . views import create , query , cart

urlpatterns = [
    path("create/" , create),
    path("query/" , query ,name = "query"),
    path("cart/" , cart ,name = "cart"),
]