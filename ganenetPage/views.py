# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from parentsPage.views import submissionsParent
from ganenetPage.forms import ReviewForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from parentsPage.models import submission
from homePage.models import subject,mashov
from django.http import HttpResponse
from .models import Review
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.models import Group, User
from parentsPage.models import submission

@login_required(login_url='/accounts/login/')

def index(request):
    return render(request,"ganenetPage.html")

def about(request):
    return render(request,"about.html")

def viewSubmission(request):
    context= {}
    Subjects= subject.objects.all()
    context= {'Subjects': Subjects}
    print(context)
    return render (request,"viewSubmission.html", context)

def Submissions(request,subjectName):
    submissions = submission.objects.all().filter(subjectName=subjectName)
    context= {'submissions': submissions}
    return render (request, "submissions.html", context)

def reviewGanenet(request):
    # reviews = Review.objects.all().filter(subjectName=subjectName)
    # context= {'reviews': reviews}
    return render (request, "review.html")
    
def add_review(request):
    if request.method == 'GET':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            #data.kidId = form.cleaned_data['kidId']
            #subjectName = Submission
            kidId = form.cleaned_data['kidId']
            subjectName = form.cleaned_data['subjectName']
            review = form.cleaned_data['review']
            form.save()
            return redirect('success')
    return render(request, "review.html", {'form': form,'submission': submission})

def successView(request):
    return render(request, "success.html")

def viewmashovs(request):
    return render(request,"viewmashovs.html")

def viewmashovss(request):
    labels = []
    data = []

    queryset = mashov.objects.values('subject__nameSubject').annotate(mashov_feedback=Sum('feedback')).order_by('-mashov_feedback')
    for entry in queryset:
        labels.append(entry['subject__nameSubject'])
        data.append(entry['mashov_feedback'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
         })

def trackinglog(request):
    users = User.objects.all().filter(groups__name='Kids')
    context= {'users': users}
    return render(request,"trackinglog.html",context)

# def addReview(request,):
#     subs= submission.objects.all().filter(kidId=kidId)
#     return render (request, "submissions.html", context)

#     if request.method == 'GET':
#         form = ReviewForm()
#     else:
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.cleaned_data['review']
            
#             new_review=form.save()
#             return redirect('success')
#     return render(request, "review.html", {'form': form})