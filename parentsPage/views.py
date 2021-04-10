from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from homePage.models import subject

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,"parentsPage.html")

def submissionsParent(request):
    return render(request,"submissionsParent.html")

