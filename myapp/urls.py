"""myapp URL Configuration

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
from . import views
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title="Django boilerplate API", default_version='v1'))

urlpatterns = [
    path(r'swagger-ui', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path(r'', views.health_check),
    path(r'user', views.UserView.as_view(), name='user'),
    path(r'helloworld', views.hello_world, name='hello_world'),
]
