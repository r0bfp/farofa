from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product
from .utils.Gmail import Gmail


def index(request):
    products = Product.objects.all()

    return render(request, "products/index.html", {'products': products})


def store(request):
    name    = request.POST.get('name') 
    code    = request.POST.get('code')
    type    = request.POST.get('type')
    message = request.POST.get('message')

    if Product.objects.filter(code=code).exists():
        messages.error(request, f'Já existe um produto com o código {code}')

        return redirect('index')

    product = Product(name=name, code=code, type=type, message=message)
    product.save()

    return redirect('index')


def delete(request, id):
    product = Product(id=id)
    product.delete()

    return redirect('index')


def order_paid(request):
    gmail = Gmail('desenvolvimento.robert@gmail.com', 'zumuvdvbzsbevibf')
    products = Product.objects.filter(name='Produto Teste')

    if not products:
        gmail.send(to='desenvolvimento.robert@gmail.com', subject='Teste', body_as_html='<h1>Produto esgotado :(</h1>')
        return HttpResponse('Nenhum produto encontrado')

    product = products[0]
    # TODO envia whatsapp com o código
    gmail.send(to='desenvolvimento.robert@gmail.com', subject='Teste', body_as_html=f'<h1>{product.code}</h1>')

    # product.delete()

    return HttpResponse('ok')