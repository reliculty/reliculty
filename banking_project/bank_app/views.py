from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm-password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'username_taken':'p'})
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                return redirect('login')

        else:
            return render(request, 'register.html', {'passwords_dont_match':'h'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        print('post acheived!')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user_page')
        else:
            return render(request, 'login.html', {'invalid_credentials':'t'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        age = request.POST['age']
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
        debit_card = 'debitCard' in request.POST
        credit_card = 'creditCard' in request.POST
        cheque_book = 'chequeBook' in request.POST
        customer = Customer(
            name=name,
            email=email,
            dob=dob,
            age=age,
            phone=phone,
            gender=gender,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            debit_card=debit_card,
            credit_card=credit_card,
            cheque_book=cheque_book
        )
        customer.save()
        return render(request, 'user.html', {'registrationSuccess': True})
        # return render(request, 'user.html', {'success':'s'})  # Redirect to a success page

    return render(request, 'user.html')

def user_page(request):
    return render(request, 'user_page.html')