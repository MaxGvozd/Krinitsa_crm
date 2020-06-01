from django.shortcuts import render, redirect

from sales.forms import AreaForm


def create_area(request):
    if request.method == 'GET':
        form = AreaForm()
        return render(request, 'area.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'area.html', context={
                "form": form
            })
