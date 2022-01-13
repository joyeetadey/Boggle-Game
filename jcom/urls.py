"""jcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.button,name="script4"),
    path('select/',views.output,name="script"),
    path('4x4/',views.output1,name="script1"),
    path('5x5/',views.output2,name="script2"),
    path('dhyani/',views.output3,name="dhyani"),    
    path('4x4/word',views.addword),
    

]

