from django.shortcuts import render, redirect, get_object_or_404
from .models import Qualifications


def index(request):
    qualifications = Qualifications.objects.all()
    return render(request, 'index.html', {'qualifications': qualifications})
