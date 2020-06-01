from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def main(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return render(request, 'main1.html')
    elif request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'main1.html')
        else:
            return render(request, 'login.html', context={
                "error": True,
            })
