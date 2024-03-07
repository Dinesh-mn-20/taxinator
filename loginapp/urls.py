"""
URL configuration for tax_calculator project.

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
from django.urls import path
from .views import my_register_page, my_login_page, addnewuser, validatelogin, my_userprofile_page, my_answering_page, AnswerQuestion

urlpatterns = [
    path('', my_login_page),
    path('register/', my_register_page),
    path('addnewuser/', addnewuser),
    path('validatelogin/', validatelogin),
    path('userprofile/', my_userprofile_page),
    path('admins/', my_answering_page),
    path('AnswerQuestion/', AnswerQuestion)
]
