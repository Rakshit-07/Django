from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import todolist

# Create your views here.
def todo(request):
    #return HttpResponse('Hello World')
    all_task = todolist.objects.all()
    context ={
        'all_task': all_task
    }
    
    #context = {'welcome_messge': 'hello from to do!'}
    return render(request, 'todolist.html', context)

def contact(request):
    #return HttpResponse('Hello contact')
    context = {'welcome_messge': 'hello from contact us!'}
    return render(request, 'contact.html', context)

def about(request):
    #return HttpResponse('Hello about')
    context = {'welcome_messge': 'hello from about us!'}
    return render(request, 'about.html', context)