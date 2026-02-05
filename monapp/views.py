from django.shortcuts import render

def accueil(request):
    return render(request, 'monapp/accueil.html')

def a_propos(request):
    return render(request, 'monapp/a_propos.html')

def contact(request):
    return render(request, 'monapp/contact.html')