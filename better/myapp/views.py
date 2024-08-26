from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# def execute_sql_file(file_path):
#     with open(file_path, 'r') as sql_file:
#         sql = sql_file.read()
# with connection.cursor() as cursor:
#         cursor.execute(sql)


def english(request):
    return render(request, 'random2.html')
def hindi(request):
    return render(request,'random22.html')
def jobs(request):
    return render(request,'random3.html')
def jobs_hindi(request):
    return render(request,'random33.html')
def apply(request):
    return render(request,'random4.html')
def feedback(request):
    return render(request,'feedback.html')
def faq(request):
    return render(request,'FAQs.html')
def sign(request):
    return render(request,'signup.html')
def calender(request):
    return render(request,'calender.html')
def all(request):
    return render(request,'gg3.html')
