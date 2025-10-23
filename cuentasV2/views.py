from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cuentas:bienvenida')  # 👈 cambio aquí
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'cuentasV2/login.html')

@login_required
def bienvenida(request):
    return render(request, 'cuentasV2/bienvenida.html', {'usuario': request.user})

def logout_view(request):
    logout(request)
    return render(request, 'cuentasV2/logout.html')
