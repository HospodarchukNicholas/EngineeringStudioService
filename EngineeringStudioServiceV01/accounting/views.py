from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def main_view(request):
    bolts = Bolt.objects.all()
    # items = Item.objects.select_related('bolt', 'nut' ).all()
    return render(request, 'accounting/main_view.html', {'bolts':bolts,})