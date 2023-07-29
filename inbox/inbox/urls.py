"""inbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from AppV2 import views #from inside app import to inbox

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # Path to access admin page
    path('admin/', admin.site.urls),
    # Path to home page (frontend)
    path('', views.home, name="home"),
    # Path to inbox page (backend)
    path('inbox/', views.inbox, name="inbox"),
    # url on browser   Function on views.py    url inside the html file
    # Path to Login/Logout
    path('login/', include('django.contrib.auth.urls')),
    path("create/", views.create_client, name="create_client"),
    path("dashboard/", views.client_dashboard, name="client_dashboard")

]