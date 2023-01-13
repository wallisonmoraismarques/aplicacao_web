"""faculdade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView
from  django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pet/all/", views.list_all_pets),
    path("pet/user/", views.list_all_pets),
    path("pet/detail/<id>/", views.pet_detail),
    path("login/", views.login_user),
    path("login/submit",views.submit_login),
    path("logout/",views.logout_user),
    path("pet/register/",views.register_pet),
    path("pet/register/submit", views.set_pet),
    path("pet/delete/<id>/", views.delete_pet),
    path("",RedirectView.as_view(url="pet/all/"))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

