from django.db.models import Q
from django.shortcuts import render, redirect

from goods.forms import WarehouseForm, ProductForm, VolumeForm
from goods.models import Warehouse, Product, Volume
from django.views.decorators.http import require_GET


@require_GET
def warehouses(request):
    query = request.GET.get("q", "")
    warehouses_list = Warehouse.objects.filter(
        Q(name__icontains=query)
    )
    return render(request, 'warehouses_list.html', context={
        "warehouses_list": warehouses_list
    })

@require_GET
def products(request):
    query = request.GET.get("q", "")
    products_list = Product.objects.filter(Q(name__icontains=query))
    return render(request, 'products_list.html', context={
        "products_list": products_list
    })

@require_GET
def volume(request):
    query = request.GET.get("q", "")
    volume_list = Volume.objects.filter(Q(name__icontains=query))
    return render(request, 'volume_list.html', context={
        "volume_list": volume_list
    })


def create_warehouse(request):
    if request.method == 'GET':
        form = WarehouseForm()
        return render(request, 'warehouse.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'warehouse.html', context={
                "form": form
            })


def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'products.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'products.html', context={
                "form": form
            })


def create_volume(request):
    if request.method == 'GET':
        form = VolumeForm()
        return render(request, 'volume.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = VolumeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'volume.html', context={
                "form": form
            })


def retrieve(request, id=None):
    if request.method == 'GET':
        product = Product.objects.get(pk=id)
        return render(request, 'retrieve.html', context={
            "product": product
        })
    elif request.method == 'POST':
         return render(request, 'congratulation.html')
