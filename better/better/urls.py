from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('random2.html', include('myapp.urls')),
    path('random3.html', include('myapp.urls')),
    path('random4.html', include('myapp.urls')),
    path('feedback.html', include('myapp.urls')),
    path('FAQs.html', include('myapp.urls')),
    path('signup.html', include('myapp.urls')),
    path('calender.html', include('myapp.urls')),
    path('gg3.html', include('myapp.urls')),
    path('random22.html', include('myapp.urls')),
    path('random33.html', include('myapp.urls')),
]
