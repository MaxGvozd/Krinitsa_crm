from django.contrib.auth import logout
from django.shortcuts import render, redirect
from users.forms import RegistrationForm


def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form
        })
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html')
        else:
            return render(request, 'register.html', context={
                "form": form
            })


def logout_user(request):
    logout(request)
    return redirect("/")
