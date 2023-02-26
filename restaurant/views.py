from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import BookingForm
from .models import Menu
from .forms import UserLoginForm



# Create your views here.
# def signin(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return HttpResponse("Wrong details")

#         login(request, user)
#         return redirect('/')
#     else:
#         form = UserLoginForm()
#         return render(request, 'login.html', {'form':form})





def home(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data
    }
    return render(request, 'menu.html', main_data)



def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    context = {
        "item": menu_item
    }
    return render(request, 'menu_item.html', context)