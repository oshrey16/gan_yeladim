# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import subForm, ContactForm, MessageForm
from django.urls import reverse
from parentsPage.models import submission
from homePage.models import Question, Choice , News, reportBug,Message
from django.core.mail import send_mail, BadHeaderError, EmailMessage

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
	
def detail(request, question_id):
    latest_question_list = Question.objects.order_by('-id')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, "detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
    
def news(requset):
    news = News.objects.all()
    con = {'news':news}
    return render(requset,"news.html",con)
	
def reportBugView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            emailAddress = form.cleaned_data['emailAddress']
            phoneNumber = form.cleaned_data['phoneNumber']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                new_mail=form.save()
                msgToHost = EmailMessage(
                    u"פנייה חדשה : "+firstName+" "+lastName,
                    subject+"\n\n"+message+"\n\n==================================\n"+emailAddress+u"   פרטים ליצירת קשר: "+phoneNumber,
                    emailAddress,
                    ['balagandevelopers@gmail.com'],
                )
                msgToSender = EmailMessage(
                     u"פנייתך בנושא : "+subject+u" נשלחה בהצלחה ",
                     u"נציג מטעמינו יצור עמך קשר בהקדם. ",
                    emailAddress,
                   [emailAddress],
                )
                msgToHost.send()
                msgToSender.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "bug.html", {'form': form})	


def MessageView(request):
    if request.method == 'GET':
        form = MessageForm()
    else:
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            emailAddress = form.cleaned_data['emailAddress']
            phoneNumber = form.cleaned_data['phoneNumber']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                new_mail=form.save()
                msgToHost = EmailMessage(
                    u"הודעה חדשה : "+firstName+" "+lastName,
                    subject+"\n\n"+message+"\n\n==================================\n"+emailAddress+u"   פרטים ליצירת קשר: "+phoneNumber,
                    emailAddress,
                    ['marinajata@gmail.com'],
                )
                msgToSender = EmailMessage(
                     u"הודעתך בנושא : "+subject+u" נשלחה בהצלחה ",
                    emailAddress,
                   [emailAddress],
                )
                msgToHost.send()
                msgToSender.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "Message.html", {'form': form})	


