from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("store/", views.store, name="store"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("order_paid/", views.order_paid, name="order_paid")
]