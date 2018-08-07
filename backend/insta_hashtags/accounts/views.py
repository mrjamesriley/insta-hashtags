from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm





def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #Read up on this part
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/categories/')
        else:
            error_messages = form.error_messages
            args = {'error_messages': error_messages}
            return render(request, 'accounts/reg_form.html', args)
    else:
        form = SignUpForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/categories/')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        return redirect('accounts/profile.html')
    return render(request, 'registration/login.html')

def test(request):
    args = {'user': request.user}
    return render(request, 'accounts/test.html', args)

