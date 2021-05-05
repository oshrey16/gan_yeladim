# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from parentsPage.models import submission
from homePage.models import subject
from django.http import HttpResponse


def index(request):
    return render(request,"ganenetPage.html")


def viewSubmission(request):
    context= {}
    Subjects= subject.objects.all()
    context= {'Subjects': Subjects}
    print(context)
    return render (request, "viewSubmission.html", context)


def Submissions(request,subjectName):
    submissions = submission.objects.all().filter(subjectName=subjectName)
    print(submissions)
    context= {'submissions': submissions}
    return render (request, "submissions.html", context)



