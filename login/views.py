from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def login_template(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        
        print(f"Username: {username}")  # Mostrar el nombre de usuario en la consola
        print(f"Password: {password}")  # Mostrar la contraseña en la consola
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("Autenticación fallida")  # Mostrar un mensaje si la autenticación falla
            
            return render(request, 'login/login.html', {'error': 'usuario y/o constraseña incorrectos'})
    return render(request,'login/login.html')
