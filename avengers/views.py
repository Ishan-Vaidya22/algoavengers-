from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection



def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')
def posts(request):
    return render(request, 'posts.html')
def loginh(request):
    return render(request, 'loginh.html')
def postsh(request):
    return render(request, 'postsh.html')
def calender(request):
    return render(request, 'calender.html')
def faq(request):
    return render(request, 'FAQs.html')
def feedback(request):
    return render(request, 'feedback.html')
def form(request):
    return render(request, 'form.html')
def signup(request):
    return render(request, 'signup.html')
def application_form2(request):
    return render(request, 'application_form2.html')

