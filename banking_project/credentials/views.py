from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm-password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                # messages.info(request, "Username is taken!")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                print('USER CREATED!')
                return redirect('login')

        else:
            messages.info(request, "Passwords do not match!")
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user')
        else:
            # messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')