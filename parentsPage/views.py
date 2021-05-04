from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import subForm
from django.urls import reverse
from parentsPage.models import submission
from homePage.models import Question, Choice , News

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

	