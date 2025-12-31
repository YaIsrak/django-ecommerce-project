from django.shortcuts import render
from django.http import HttpResponse
from .form import SignUpForm
from .models import Account
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.phone_number = phone_number
            user.save()

            messages.success(request, 'Your account has been created successfully.')
            return redirect('sign_up')
    else:
        form = SignUpForm()

    context = {'form': form}

    return render(request, 'accounts/sign-up.html', context)

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('sign_in')
    return render(request, 'accounts/sign-in.html')

@login_required(login_url='sign_in')
def signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('sign_in')