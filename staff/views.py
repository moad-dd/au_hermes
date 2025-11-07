from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Fonctionnaire, Employee
from .forms import FonctionnaireForm, EmployeeForm

@login_required
def onboard_employee(request):
    """Onboarding form for users missing Employee record"""
    if Employee.objects.filter(user=request.user).exists():
        return redirect('staff:ats_space')

    if request.method == 'POST':
        position = request.POST.get('position', '').strip()
        department = request.POST.get('department', '').strip()
        base_salary = request.POST.get('base_salary', '0').strip()
        bonus = request.POST.get('bonus', '0').strip()
        deductions = request.POST.get('deductions', '0').strip()

        if position and base_salary:
            emp = Employee.objects.create(
                user=request.user,
                position=position,
                department=department,
                base_salary=base_salary or 0,
                bonus=bonus or 0,
                deductions=deductions or 0,
            )
            messages.success(request, 'Onboarding complete! You can now access Administrative Staff Services.')
            return redirect('staff:ats_space')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'staff/onboard_employee.html')

@login_required
def civil_servants_list(request):
    """List all civil servants with search and pagination"""
    query = request.GET.get('q', '')
    fonctionnaires = Fonctionnaire.objects.all()
    
    if query:
        fonctionnaires = fonctionnaires.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(ss__icontains=query) |
            Q(grade__icontains=query)
        )
    
    paginator = Paginator(fonctionnaires, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'fonctionnaires': page_obj,
        'query': query,
        'show_footer': True,
    }
    return render(request, 'staff/civil_servants_list.html', context)

@login_required
def civil_servant_detail(request, pk):
    """View detailed information about a civil servant"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    context = {
        'fonctionnaire': fonctionnaire,
    }
    return render(request, 'staff/civil_servant_detail.html', context)

@login_required
def add_civil_servant(request):
    """Add a new civil servant"""
    if request.method == 'POST':
        form = FonctionnaireForm(request.POST, request.FILES)
        if form.is_valid():
            fonctionnaire = form.save()
            messages.success(request, 'Civil servant added successfully!')
            return redirect('staff:civil_servants_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FonctionnaireForm()
    
    context = {
        'form': form,
        'title': 'Add Civil Servant',
        'button_text': 'Add',
    }
    return render(request, 'employees/civil_servant_form.html', context)

@login_required
def edit_civil_servant(request, pk):
    """Edit an existing civil servant"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = FonctionnaireForm(request.POST, request.FILES, instance=fonctionnaire)
        if form.is_valid():
            form.save()
            messages.success(request, 'Civil servant updated successfully!')
            return redirect('staff:civil_servants_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FonctionnaireForm(instance=fonctionnaire)
    
    context = {
        'form': form,
        'title': 'Edit Civil Servant',
        'button_text': 'Update',
        'fonctionnaire': fonctionnaire,
    }
    return render(request, 'employees/civil_servant_form.html', context)

@login_required
def delete_civil_servant(request, pk):
    """Delete a civil servant"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    fonctionnaire.delete()
    messages.success(request, 'Civil servant deleted successfully!')
    return redirect('staff:civil_servants_list')

@login_required
def list_ats(request):
    """List all administrative staff (ATS)"""
    query = request.GET.get('q', '')
    employees = Employee.objects.select_related('user').all()
    
    if query:
        employees = employees.filter(
            Q(user__username__icontains=query) |
            Q(position__icontains=query) |
            Q(department__icontains=query)
        )
    
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'employees': page_obj,
        'query': query,
        'show_footer': True,
    }
    return render(request, 'staff/ats_list.html', context)

@login_required
def delete_ats(request, pk):
    """Delete an administrative staff member"""
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'Administrative staff deleted successfully!')
    return redirect('staff:list_ats')

@login_required
def user_space(request):
    """User space for managing civil servants"""
    query = request.GET.get('q', '')
    fonctionnaires = Fonctionnaire.objects.all().order_by('-date_rec')
    
    if query:
        fonctionnaires = fonctionnaires.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query)
        )
    
    context = {
        'users': fonctionnaires,
        'query': query,
    }
    return render(request, 'staff/user_space.html', context)

@login_required
def ats_space(request):
    """ATS space for administrative staff features"""
    return render(request, 'staff/ats_space.html')
