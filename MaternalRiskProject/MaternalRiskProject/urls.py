"""
URL configuration for MaternalRiskProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import chatbot
# from MaternalRiskProject.views import chatbot

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("predict/", views.predict),
    path("predict2/", views.predict2),
    path("hello/", views.hello),
    path("predict/result", views.result),
    path("predict2/result", views.mentalresult),
    path('hello/answer', views.chatbot),
    path('chatbot/', chatbot, name='chatbot'),

]





