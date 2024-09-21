
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home.html'),
    path('login.html', views.login, name='login'),
    path('posts.html', views.posts, name='posts'),
    path('loginhhtml', views.loginh, name='loginh'),
    path('postsh.html', views.postsh, name='postsh'),
    path('calender.html', views.calender, name='calender'),
    path('faq.html', views.faq, name='faq.html'),
    path('feedback.html', views.feedback, name='feedback'),
    path('form.html', views.form, name='form'),
    path('signup.html', views.signup, name='signup'),
    path('application_form2.html', views.application_form2, name='application_form2')
]