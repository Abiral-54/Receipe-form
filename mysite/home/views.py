from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'abiral', 'age': 22},
        {'name': 'sandesh', 'age': 19},
        {'name': 'anukul', 'age': 17},
        {'name': 'abishek', 'age': 25},
        {'name': 'paras', 'age': 15},
    ]
    vegetables=['pumkin','tomato','potato']

    return render(request,"index.html", context = {'peoples' : peoples, 'vegetables' : vegetables})

def about(request):
    return HttpResponse("Hey! this is a about page")

def contact(request):
    return HttpResponse("Hey! this is a contact page")