from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def index(request):
    items = Product.objects.all()
    return render(request,'app/index.html',{'items':items})

def detail(request,id):
    item = Product.objects.get(id=id)
    return render(request,'app/detail.html',{'item':item})

'''def create_product(request):
    product_form = ProductForm(request.POST or None)
    if product_form.is_valid():
        product_form.save()
        return redirect('/')
    return render(request,'app/create_form.html',{'product_form':product_form})'''

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None)
        if product_form.is_valid():
            product_form.save()
            return redirect('/')
    else:
        product_form = ProductForm()
    return render(request,'app/create_form.html',{'product_form':product_form})
    
def update_product(request,id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST or None, instance=product)
    if product_form.is_valid():
        product_form.save()
        return redirect('/')
    return render(request,'app/create_form.html',{'product':product,'product_form':product_form})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    return render(request,'app/delete.html',{'product':product})