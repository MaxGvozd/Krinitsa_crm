from django.shortcuts import render, get_object_or_404

from events.forms import SaleForm
from events.models import Sale
from goods.models import Product, Warehouse
from companies.models import Company, Outlet


def crate_sale(request):
    # if request.method == 'GET':
    #     products = Product.objects.all()
    #     companies = Company.objects.all()
    #     outlets = Outlet.objects.all()
    #     warehouses = Warehouse.
    #     print(outlets)
    #     return render(request, 'sale.html', context={
    #         "products": products,
    #         "companies": companies,
    #         "outlets": outlets,
    #         "warehouses": warehouses
    #     })

    if request.method == 'GET':
        form = SaleForm()
        return render(request, 'sale.html', context={
            'form': form
        })

    # elif request.method == 'POST':
    #     warehouse = request.warehouse
    #     company = request.company
    #     product = request.product
    #     outlet = request.outlet
    #     user = request.user
    #     Sale.objects.create(
    #         company=company,
    #         outlet=outlet,
    #         warehouse=warehouse,
    #         product=product,
    #         created_by=user
    #     )
    #     return render(request, 'congratulation.html')
    elif request.method == 'POST':
        form = SaleForm(request.POST)
        form.user = request.user
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'sale.html', context={
                "form": form
            })


def sale(request):
    sale_list = Sale.objects.all()
    return render(request, 'sale_list.html', context={
        "sale_list": sale_list
    })


def product_list(request, category_slug=None):
    #category = None
    #categories = Volume.objects.all()
    products = Product.objects.all()
    return render(request, 'sale.html', context={
        "products": products
    })
    # if category_slug:
    #     category = get_object_or_404(Volume, slug=category_slug)
    #     products = products.filter(volume=category)
    # return render(request,
    #               'shop/product/list.html',
    #               {'category': category,
    #                'categories': categories,
    #                'products': products})