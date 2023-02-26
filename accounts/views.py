from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

# Using Class based Views
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# using function based views

def registerUser(request):
    # form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("/")
        messages.error(request, "Registration Unsuccessful.")
    form = NewUserForm()
    return render(request, "registration/register.html", {"form": form})
