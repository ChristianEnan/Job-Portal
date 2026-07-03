from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(request, "accounts/register.html", {
        "form": form
    })


def user_login(request):

    error = ""

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("home")

        else:

            error = "Invalid Username or Password"

    return render(request,
                  "accounts/login.html",
                  {
                      "error": error
                  })


def user_logout(request):

    logout(request)

    return redirect("home")