from django.shortcuts import render
from django.http import HttpResponse
from .form import SignUpForm
from .models import Account

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
    else:
        form = SignUpForm()

    context = {'form': form}

    return render(request, 'accounts/sign-up.html', context)

def signin(request):
    return render(request, 'accounts/sign-in.html')

def signout(request):
    return render(request, 'accounts/sign-out.html')