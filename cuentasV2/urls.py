from django.urls import path
from . import views

app_name = 'cuentas'  # 👈 AGREGA ESTA LÍNEA

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('logout/', views.logout_view, name='logout'),
]
