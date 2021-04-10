from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import subForm
from parentsPage.models import submission

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,"parentsPage.html")

def submissionsParent(request):
    return render(request,"submissionsParent.html")

def subView(request):
    if request.method == 'GET':
        form = subForm()
    else:
        form = subForm(request.POST, request.FILES)
        if form.is_valid():
            kidId = form.cleaned_data['kidId']
            subjectName = form.cleaned_data['subjectName']
            submissions = form.cleaned_data['submissions']
            new_sub=form.save()
            return redirect('success')
    return render(request, "sub.html", {'form': form})

def successView(request):
    return render(request, "success.html")