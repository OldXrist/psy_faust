from django.shortcuts import render
from .models import Qualifications, FAQ, Contacts


def index(request):
    qualifications = Qualifications.objects.all()
    faq = FAQ.objects.all()
    contacts = Contacts.objects.first()
    return render(request, 'index.html', {'qualifications': qualifications, 'FAQ': faq, 'contacts': contacts})
