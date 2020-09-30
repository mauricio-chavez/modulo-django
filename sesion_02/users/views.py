from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def sign_in(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('movies:list')
        else:
            context['error'] = 'Credenciales inválidas'
    return render(request, 'users/login.html', context)


def log_out(request):
    logout(request)
    return redirect('users:login')
