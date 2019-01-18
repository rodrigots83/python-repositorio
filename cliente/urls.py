"""meuPrimeiroProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import persons_list, persons_new, persons_update, persons_delete

urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', persons_new, name='person_new'),
    path('update/<int:id>/', persons_update, name='person_update'),
    path('delete/<int:id>/', persons_delete, name='person_delete'),
]