from django.shortcuts import render
from .models import Qualifications, FAQ


def index(request):
    qualifications = Qualifications.objects.all()
    faq = FAQ.objects.all()
    return render(request, 'index.html', {'qualifications': qualifications, 'FAQ': faq})
