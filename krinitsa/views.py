from django.shortcuts import render


def main(request):
    user = request.user
    return render(request, 'main1.html')
