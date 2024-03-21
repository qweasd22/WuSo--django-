from django.shortcuts import render, redirect
from  django.http import *
from .models import Food, Cart
from .mixinin import DataMixin
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import Reg_User_Form, Auth_User_Form
from django.urls import reverse_lazy
from django.template import loader

def index(request):
     foods = Food.objects.all()
     cards = []
     for food in foods:
          card = '''<div class="CARD">
                <img src="{0}">
                <div class="Info">
                    <h2>{1}</h2>
                    <div class="Count-Info">
                        <p>{2}шт</p>
                        <p>{3}г</p>
                    </div>
                </div>
                <h1>{4}</h1>
                <p>{5}</p>
                <button onclick="GET_FOOD({7})">В корзину за {6}₽</button>
            </div>'''
          card = card.format(f"static/RES/{food.image}", food.type, food.count, food.weight, food.name, food.structure, food.price, food.id)
          cards.append(card)
          cards.reverse()

     return render(request, "HOME/index.html", context={"cards": cards})

from django.shortcuts import render, get_object_or_404


def product(request, product_id):
    food = get_object_or_404(Food, id=product_id)
    data = {
        'IMAGE': f'/static/RES/{food.image}',
        'TYPE': food.type,
        'COUNT': food.count,
        'WEIGHT': food.weight,
        'NAME': food.name,
        'ABOUT': food.structure,
        'TEXT': food.text,
        'PRICE': food.price,
        'ID': food.id
    }
    return render(request, "PRODUCT/PRODUCT.html", context=data)


def add_cart(request, product_id):
    try:
        user = request.user
        food = Food.objects.filter(id = int(product_id))[0]
        print(user, food, product_id)
        try:
            
            cart = Cart.objects.get(user = user)
            print(cart)
            product = cart.product
            print(product)
            product_1 = cart.product.split(":")[:-1]
            try:
                for p in product_1:
                    p = p.split("|")
                    if str(p[0][1:]) == str(food.id):
                        cart.product = cart.product
                        cart.total_price = f"{int(cart.total_price) + int(food.price)}"
            except Exception as e:
                print(e)
                cart.product += f"[{food.id}|1]:"
                cart.total_price = f"{int(cart.total_price) + int(food.price)}"
                cart.save()            

        except Exception as e:
            cart = Cart.objects.create(
                user = user,
                product = f"[{food.id}|1]:",
                total_price = f"{food.price}"
            )
            print(cart)
            cart.save()
        return redirect("home")
    except:
        return redirect("home")
    
def clear_cart(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    cart.product = ""
    cart.save()

def cart(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    product = cart.product.split(":")[:-1]
    print(product)
    foods = []
    for p in product:
        print(p)
        p = p.split("|")
        id = int(p[0][1:])
        print("ID - ",id)
        food = Food.objects.get(id = id)
        print("Food - ", food)
        count = p[1][:-1]
        res = f"<h1>Еда: {food.name} | Количество: {count}</h1>"
        foods.append(res)
    foods.append(f"<h1>Итого: {cart.total_price}</h1>")
    return render(request, "CART/CART.html", context={"cards": foods})

def debug_templates(request):
    return render(request, "debug_template.html")

def home(request):
    new_url = f'/'
    return redirect(new_url)

def close(request):
    new_url = 'home/'
    return redirect(new_url)

def logout_user(request):
    logout(request)
    return redirect("home")


class Reg_User(DataMixin, CreateView):
    form_class = Reg_User_Form
    template_name = 'REG/REG.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class Auth_User(DataMixin, LoginView):
    form_class = Auth_User_Form
    template_name = 'AUT/AUT.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy("home")
    
