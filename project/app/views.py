from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Order, Statement, Medication
from django.contrib.auth.forms import UserCreationForm
from . forms import OrderForm, CreateUserForm
# Create your views here.
def index(request):
    #homes = Home.objects.all()
    return render(request, "home.html")

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def order(request):
    if request.method == 'POST':
        medication_id = request.POST.get('medication')
        quantity = int(request.POST.get('quantity'))
        medication = Medication.objects.get(pk=medication_id)
        if medication.stock_quantity >= quantity:
            order = Order.objects.create(
                customer=request.user,
                medication=medication,
                quantity=quantity,
                is_confirmed=False,
                is_paid=False
            )
            # Update stock quantity
            medication.stock_quantity -= quantity
            medication.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_history')
        else:
            messages.error(request, 'Insufficient stock for the selected medication.')
    medications = Medication.objects.all()
    return render(request, "place_order.html", {'medications': medications})

def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'order_history.html', {'orders': orders})

def statement(request):
    statements = Statement.objects.filter(customer=request.user)
    return render(request, 'statement.html', {'statements': statements})