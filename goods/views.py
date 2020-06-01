from django.shortcuts import render, redirect

from goods.forms import WarehouseForm, ProductForm, VolumeForm


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
            return redirect('/')
        else:
            return render(request, 'warehouse.html', context={
                "form": form
            })


def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'product.html', context={
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
            return redirect('/')
        else:
            return render(request, 'volume.html', context={
                "form": form
            })
