# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings



def index(request):
    template = 'home/home_index.html'
    context = {}
    return render(request, template, context)
