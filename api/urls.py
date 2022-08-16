"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django.http import JsonResponse

def apiIndex(req):

    return JsonResponse({'msg': 'The api index'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', apiIndex),
    path('api/tracks/', include('api.tracks.urls')),
    path('log-in/', include('users.urls')),
    # path('api/bullets/', include('api.bullets.urls')),
    # path('api/streaks/', include('api.streaks.urls')),
]



