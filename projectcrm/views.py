from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login feito com sucesso.')
            return redirect('home')
        else:
            messages.success(request, 'Erro ao fazer login, tente novamente.')
            return redirect('home')
    else:
        return render(request, 'home.html',{})


def user_logout(request):
    logout(request)
    messages.success(request, 'Desconectado com sucesso.')
    return redirect('home')