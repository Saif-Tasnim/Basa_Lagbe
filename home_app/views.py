from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'Components/AboutUspage.html')


def contact(request):
    return render(request, 'Components/Contactuspage.html')


def featured(request):
    return render(request, 'Components/FeaturedPage.html')



