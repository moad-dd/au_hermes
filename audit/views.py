from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Historique
from staff.models import Fonctionnaire


@login_required
def view_history(request, pk):
    """View action history for a civil servant"""
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    historique = Historique.objects.filter(fonctionnaire=fonctionnaire).order_by('-date_action')
    
    context = {
        'fonctionnaire': fonctionnaire,
        'historique': historique,
    }
    return render(request, 'audit/view_history.html', context)
