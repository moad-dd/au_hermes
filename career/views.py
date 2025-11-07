from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from .models import CareerHistory, Promotion, Echelon
from .forms import PromotionForm, EchelonForm
from staff.models import Fonctionnaire
from audit.models import Historique


@login_required
def career_history(request):
    """View career history for administrative staff"""
    try:
        employee = request.user.employee
    except:
        return redirect('onboard_employee')
    
    history = CareerHistory.objects.filter(employee=employee).order_by('-start_date')
    context = {
        'employee': employee,
        'history': history,
    }
    return render(request, 'career/career_history.html', context)


@login_required
def update_promotion(request, pk):
    """Add/Update promotion for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.fonctionnaire = fonctionnaire
            promotion.save()
            
            # Update the current grade
            fonctionnaire.grade = promotion.nouveau_grade
            fonctionnaire.save()
            
            Historique.objects.create(
                fonctionnaire=fonctionnaire,
                type_action='Promotion',
                details=f'Promu au grade: {promotion.nouveau_grade}',
                user=request.user
            )
            
            messages.success(request, 'Promotion added successfully!')
            return redirect('civil_servant_detail', pk=pk)
    else:
        form = PromotionForm(initial={'ancien_grade': fonctionnaire.grade})
    
    context = {
        'form': form,
        'fonctionnaire': fonctionnaire,
        'title': 'Update Promotion',
    }
    return render(request, 'career/update_promotion.html', context)


@login_required
def update_grade_level(request, pk):
    """Add/Update grade level for civil servants"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    
    if request.method == 'POST':
        form = EchelonForm(request.POST)
        if form.is_valid():
            echelon = form.save(commit=False)
            echelon.fonctionnaire = fonctionnaire
            echelon.save()
            
            Historique.objects.create(
                fonctionnaire=fonctionnaire,
                type_action='Changement Échelon',
                details=f'Nouvel échelon: {echelon.nouvel_echelon}',
                user=request.user
            )
            
            messages.success(request, 'Grade level updated successfully!')
            return redirect('civil_servant_detail', pk=pk)
    else:
        form = EchelonForm()
    
    context = {
        'form': form,
        'fonctionnaire': fonctionnaire,
        'title': 'Update Grade Level',
    }
    return render(request, 'career/update_grade_level.html', context)


@login_required
def print_work_certificate(request, pk):
    """Print work certificate"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    context = {
        'fonctionnaire': fonctionnaire,
        'now': date.today(),
    }
    return render(request, 'career/print_work_certificate.html', context)
