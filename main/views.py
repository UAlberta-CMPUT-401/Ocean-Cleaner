from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    context = {'title': 'Home'} # add more stuff here

    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    # Other programs can be called here and we can output the results on the page by providing it in the dictionary
    return render(request, 'about.html', context)