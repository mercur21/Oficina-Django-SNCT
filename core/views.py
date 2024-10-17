from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from core.forms import RegistroForm

def index(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/index.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirecione para uma página após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'core/login.html')