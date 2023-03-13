from django.shortcuts import render, redirect,get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.core.mail import send_mail
from .utils import generate_random_code
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'signup.html', {'form': form})

@login_required
def sentemail(request):
    # Send confirmation email
    code = generate_random_code()
    send_mail(
        'Confirm your email',
        f'Your confirmation code is: {code}',
        'example@gmail.com',
        [request.user.email],
        fail_silently=False,
    )
    # Store the code in the session
    request.session['confirmation_code'] = code
    return redirect('success')


def success(request):
        # Verify confirmation code
    code = request.POST.get('code')
    stored_code = request.session.get('confirmation_code')
    if code == stored_code:
            # Code is correct, do something
        return render(request, 'home.html')
    else:
            # Code is incorrect, show error message
        return render(request, 'confirmation.html', {'error': 'Invalid code'})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('confirm-email')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')













    