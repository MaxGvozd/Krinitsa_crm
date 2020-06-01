from django.shortcuts import render


def sale(request):
    return render(request, 'sale.html')
