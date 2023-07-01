from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


def index(request):
    products = Product.objects.all().values()
    products_fields = products[0].keys()

    print

    return render(request, "products/index.html", {'products_fields': products_fields, 'products': products})