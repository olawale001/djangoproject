from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Product, Ingredient, Sale


def home(req):
    product = Product.objects.all()
    return render(req, 'home.html', {'product': product})
    # return render(req, 'inventory/home.html')
def signup(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(req, 'signup.html', {'form': form})


def login_view(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(req, 'login.html', {'form': form})




def logout_view(req):
    if req.method == 'POST':
      logout(req)
      return redirect('home')
    

def product_list(req):
    product = Product.objects.all() 
    return render(req, 'product_list.html', {'product': product})


def ingredient_list(req):
    ingredient = Ingredient.objects.all() 
    return render(req, 'ingredient_list.html', {'ingredient': ingredient})


def record_sale(req):
    if req.method == 'POST':
        product = Product.objects.get(id=req.POST['product'])
        quantity = int(req.POST['quantity'])
        total_price = product.price * quantity
        Sale.objects.create(product=product, quantity=quantity, date=req.POST['date'], total_price=total_price)
        return redirect('ingredient_list')
    else:
        product = Product.objects.all()
        return render(req,'record_sale.html', {'product': product})
    
def record_order(req):
    if req.method == 'POST':
        ingredient = Ingredient.objects.get(id=req.POST['ingredient'])
        quantity = int(req.POST['quantity'])
        Ingredient.objects.filter(id=ingredient.id).update(quantity=ingredient.quantity - quantity)
        return redirect('ingredient_list')
    else:
        ingredient = Ingredient.objects.all()
        return render(req,'record_order.html', {'ingredient': ingredient})
