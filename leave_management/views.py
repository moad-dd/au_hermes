from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LeaveRequest, Conge
from .forms import LeaveRequestForm, CongeForm
from staff.models import Fonctionnaire
from audit.models import Historique


@login_required
def leave_request(request):
    """Submit and view leave requests for administrative staff"""
    try:
        employee = request.user.employee
    except:
        return redirect('onboard_employee')
    
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee
            leave.save()
            messages.success(request, 'Your leave request has been submitted successfully.')
            return redirect('leave_request')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LeaveRequestForm()
    
    user_requests = LeaveRequest.objects.filter(employee=employee).order_by('-date_submitted')
    context = {
        'form': form,
        'user_requests': user_requests,
    }
    return render(request, 'leave_management/leave_request.html', context)


@login_required
def update_leave(request, pk):
    """Add leave record for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = CongeForm(request.POST)
        if form.is_valid():
            conge = form.save(commit=False)
            conge.fonctionnaire = fonctionnaire
            conge.save()
            
            Historique.objects.create(
                fonctionnaire=fonctionnaire,
                type_action='Ajout Congé',
                details=f'Congé ajouté: {conge.type_conge}',
                user=request.user
            )
            
            messages.success(request, 'Leave record added successfully!')
            return redirect('civil_servant_detail', pk=pk)
    else:
        form = CongeForm()
    
    context = {'form': form, 'fonctionnaire': fonctionnaire}
    return render(request, 'leave_management/update_leave.html', context)


@login_required
def print_leave_certificate(request, pk):
    """Print leave certificate for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    conge = Conge.objects.filter(fonctionnaire=fonctionnaire).order_by('-date_debut').first()
    
    if not conge:
        messages.warning(request, 'No leave record found for this employee.')
        return redirect('civil_servant_detail', pk=pk)
    
    context = {'conge': conge}
    return render(request, 'leave_management/print_leave_certificate.html', context)
