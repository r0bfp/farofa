from django.shortcuts import render, HttpResponse, redirect
from .models import Product


def index(request):
    products = Product.objects.all()

    return render(request, "products/index.html", {'products': products})


def store(request):
    name    = request.POST.get('name') 
    code    = request.POST.get('code')
    type    = request.POST.get('type')
    message = request.POST.get('message')

    product = Product(name=name, code=code, type=type, message=message)
    product.save()

    return redirect('index')


def delete(request, id):
    product = Product(id=id)
    product.delete()

    return redirect('index')


def edit(request, id):

    return redirect('index')
