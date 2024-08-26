from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.all, name='home'),
    path('random2.html', views.english, name='login'),
    path('random22.html', views.hindi, name='login_hindi'),
    path('random3.html', views.jobs, name='posts'),
    path('random33.html', views.jobs_hindi, name='posts_hindi'),
    path('apply.html', views.apply, name='apply'),
    path('feedback.html', views.feedback, name='feedback'),
    path('FAQs.html', views.faq, name='faqs'),
    path('signup.html', views.sign, name='signup'),
    path('calendar.html', views.calender, name='view_schedule'),
]

