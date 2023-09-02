from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, update_session_auth_hash, logout
from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginUserForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from shop.models import Category
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    categories = Category.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form': form, 'categories': categories}

    return render(request, "register.html", context=context)


def my_login(request):
    categories = Category.objects.all()
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form, 'categories': categories}
    return render(request, 'my-login.html', context=context)


def my_logout(request):
    auth.logout(request)
    return redirect('shop:home')


@login_required(login_url="login")
def dashboard(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'dashboard.html', context=context)


@login_required(login_url="login")
def profile_management(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()

            # Handle password change
            old_password = user_form.cleaned_data.get('old_password')
            new_password = user_form.cleaned_data.get('new_password1')

            if old_password and new_password:
                request.user.set_password(new_password)  # Use request.user to access the logged-in user
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the session with the new password

            # Check if the user wants to delete their account
            confirm_delete = request.POST.get('confirm_delete')
            if confirm_delete:
                request.user.delete()  # Delete the user account
                logout(request)  # Log the user out after deleting the account
                return redirect('shop:home')  # Redirect to the login page after account deletion

            return redirect('dashboard')

    else:
        user_form = UpdateUserForm(instance=request.user)

    context = {'user_form': user_form, 'categories': categories}
    return render(request, 'profile-management.html', context)


@login_required(login_url="login")
def delete_account(request):
    return render(request, 'delete-account.html')
