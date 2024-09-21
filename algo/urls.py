"""
URL configuration for algo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('avengers.urls')),
    path('login.html', include('avengers.urls')),
    path('posts.html', include('avengers.urls')),
    path('form.html', include('avengers.urls')),
    path('feedback.html', include('avengers.urls')),
    path('FAQs.html', include('avengers.urls')),
    path('signup.html', include('avengers.urls')),
    path('calender.html', include('avengers.urls')),
    path('home.html', include('avengers.urls')),
    path('loginh.html', include('avengers.urls')),
    path('postsh.html', include('avengers.urls')),
    path('application_form2.html', include('avengers.urls')),
    path('admin/', admin.site.urls),
]
