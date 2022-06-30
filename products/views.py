from django.http import HttpResponse
from django.shortcuts import render
from . models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_product(request):
    return HttpResponse('Hi I am new')

