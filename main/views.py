from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        products_list = Products.objects.all()
    elif filter_type == "sepatu":
        products_list = Products.objects.filter(category="sepatu")
    elif filter_type == "bola":
        products_list = Products.objects.filter(category="bola")
    elif filter_type == "jersey":
        products_list = Products.objects.filter(category="jersey")
    elif filter_type == "celana":
        products_list = Products.objects.filter(category="celana")
    elif filter_type == "baju":
        products_list = Products.objects.filter(category="baju")
    else:
        products_list = Products.objects.filter(user=request.user)
    context = {
        'nama_aplikasi' : 'Kapuas Sportswear',
        'nama': 'Faiz Kusumadinata',
        'kelas': 'PBP A',
        'products_list' : products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        products_entry = form.save(commit=False)
        products_entry.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.increment_sales()

    context = {
        'products': products
    }

    return render(request, 'products_details.html', context)


def show_xml(request):
     products_list = Products.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
   try:
       products_item = Products.objects.filter(pk=products_id)
       xml_data = serializers.serialize("xml", products_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Products.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, products_id):
   try:
       products_item = Products.objects.get(pk=products_id)
       json_data = serializers.serialize("json", [products_item])
       return HttpResponse(json_data, content_type="application/json")
   except Products.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def update_products(request, id):
    products = get_object_or_404(Products, pk=id)
    form = ProductsForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "update_products.html", context)

def delete_product(request, id):
    products = get_object_or_404(Products, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))