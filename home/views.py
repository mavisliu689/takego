from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
def index(request):
    """
        get index.html
    """
    template = 'index.html'
    context = {}

    return render(request, template, context)



def about(request):
    """
        get about.html
    """
    template = 'about.html'
    context = {}

    return render(request, template, context)



def work(request):
    """
        get work.html
    """
    template = 'wrok.html'
    context = {}

    return render(request, template, context)