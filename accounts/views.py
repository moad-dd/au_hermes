from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserEditForm
from .models import CustomUser


def login_view(request):
    """Handle user login"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            
            return redirect("employee_dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "accounts/login.html")


def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required
def employee_dashboard(request):
    """Employee dashboard view"""
    context = {
        'user': request.user,
    }
    return render(request, "accounts/employee_dashboard.html", context)


@login_required
def admin_dashboard(request):
    """Admin dashboard view"""
    if not request.user.is_admin:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('employee_dashboard')
    
    context = {
        'total_users': CustomUser.objects.count(),
        'recent_users': CustomUser.objects.order_by('-date_joined')[:5],
    }
    return render(request, "accounts/admin_dashboard.html", context)


@login_required
def edit_account(request):
    """Allow users to edit their own account"""
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('employee_dashboard')
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'accounts/edit_account.html', {'form': form})


@login_required
def user_profile(request, username):
    """View user profile"""
    from django.shortcuts import get_object_or_404
    user = get_object_or_404(CustomUser, username=username)
    
    context = {
        'profile_user': user,
    }
    return render(request, 'accounts/user_profile.html', context)