from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginUserForm, UpdateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("shop:home")

    context = {'form': form}

    return render(request, "register.html", context=context)


def my_login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'my-login.html', context=context)


def my_logout(request):
    auth.logout(request)
    return redirect('shop:home')


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url="my-login")
def profile_management(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect ('dashboard')

    user_form = UpdateUserForm(instance=request.user)
    context = {'user_form':user_form}

    return render(request, 'profile-management.html', context)


@login_required(login_url="my-login")
def delete_account(request):
    return render(request, 'delete-account.html')
