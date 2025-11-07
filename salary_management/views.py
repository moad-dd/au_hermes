from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Paie, Prime
from .forms import PaieForm, PrimeForm
from staff.models import Fonctionnaire, Employee
from audit.models import Historique


@login_required
def salary_slip(request):
    """View salary slip for administrative staff"""
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        return redirect('onboard_employee')

    context = {'employee': employee}
    return render(request, 'employees/ats_space/salary_slip.html', context)


@login_required
def update_salary(request, pk):
    """Add/Update salary information for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = PaieForm(request.POST)
        if form.is_valid():
            paie = form.save(commit=False)
            paie.fonctionnaire = fonctionnaire
            paie.save()
            
            Historique.objects.create(
                fonctionnaire=fonctionnaire,
                type_action='Mise à jour Paie',
                details=f'Paie ajoutée pour {paie.mois}/{paie.annee}',
                user=request.user
            )
            
            messages.success(request, 'Salary information updated successfully!')
            return redirect('civil_servant_detail', pk=pk)
    else:
        form = PaieForm()
    
    context = {'form': form, 'fonctionnaire': fonctionnaire}
    return render(request, 'salary_management/update_salary.html', context)


@login_required
def update_bonus(request, pk):
    """Add bonus for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            prime = form.save(commit=False)
            prime.fonctionnaire = fonctionnaire
            prime.save()
            
            Historique.objects.create(
                fonctionnaire=fonctionnaire,
                type_action='Ajout Prime',
                details=f'Prime ajoutée: {prime.type_prime}',
                user=request.user
            )
            
            messages.success(request, 'Bonus added successfully!')
            return redirect('civil_servant_detail', pk=pk)
    else:
        form = PrimeForm()
    
    context = {'form': form, 'fonctionnaire': fonctionnaire}
    return render(request, 'salary_management/update_bonus.html', context)


@login_required
def print_salary_slip(request, pk):
    """Print salary slip for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    paie = Paie.objects.filter(fonctionnaire=fonctionnaire).order_by('-annee', '-mois').first()
    
    if not paie:
        messages.warning(request, 'No salary record found for this employee.')
        return redirect('civil_servant_detail', pk=pk)
    
    context = {
        'fonctionnaire': fonctionnaire,
        'paie': paie,
    }
    return render(request, 'salary_management/print_salary_slip.html', context)
