# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from parentsPage.models import submission
from homePage.models import subject,mashov
from django.http import HttpResponse
from .models import Review
from django.db.models import Sum
from django.http import JsonResponse


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
    
def add_review(request, subjectName):
    #Submission= submission.objects.all().filter(subjectName=subjectName)
    if request.method == 'GET':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            #data.kidId = form.cleaned_data['kidId']
            #subjectName = Submission
            review = form.cleaned_data['review']
            form.save()
            return redirect('success')
    return render(request, "review.html", {'form': form})

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