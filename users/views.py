from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from users.models import User
from django.views.decorators.http import require_GET


@require_GET
def users(request):
    query = request.GET.get("q", "")
    users_list = User.objects.filter(Q(username__icontains=query))
    return render(request, 'users_list.html', context={
            "users_list": users_list
        })


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
            return render(request, 'congratulation.html')
        else:
            return render(request, 'register.html', context={
                "form": form
            })


def logout_user(request):
    logout(request)
    return redirect("/")
