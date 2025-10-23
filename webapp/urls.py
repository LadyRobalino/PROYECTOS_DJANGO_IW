from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('cuentas:login')),
    path('admin/', admin.site.urls),
    path('', include('cuentasV2.urls')),
]
