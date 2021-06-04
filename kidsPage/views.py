from django.db.models.expressions import Value
from django.db.models.fields import CharField
from django.db.models.functions.datetime import ExtractDay, ExtractHour, TruncSecond
from django.forms.widgets import CheckboxSelectMultiple
from ganenetPage.models import Review
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from django.contrib import messages
from homePage.models import mashov, subject, Meeting,kid
import datetime
from django.db.models.functions import Extract


@login_required(login_url='/accounts/login/')

def index(request):
	if (datetime.datetime.now().day==datetime.datetime.now().day) and (datetime.datetime.now().month==datetime.datetime.now().month):
		messages.info(request,'מזל טוב ליום הולדתך!')
	return render(request,"kidsPage.html")
	

def meetings(request,Meeting_id):
	meetings_list = Meeting.objects.order_by('-id')[:20]
	context = {'meetings_list': meetings_list}
	return render(request, "Meetings.html", context)
	
def contents(request, subject_id):
	data = subject.objects.all()
	data_mashov = mashov.objects.all()
	sub = {
	"subject_id": data,
	"mashov": data_mashov
	}
	return render(request,"subject.html", sub)

def about(request):
    return render(request,"about.html")
	
def download_file(request,fl_path):
	data = subject.objects.all()
	sub = {
    "subject_id": data
	}
	subind = -1
	for index, item in enumerate(sub['subject_id']):
		if (str(item).lower()==fl_path):
			subind=index
	fl_path = data.values('submissions')[subind]['submissions']
	filename = fl_path.split('/')[1]
	fl = open(fl_path, 'r')
	response = HttpResponse(fl, content_type='application/pdf')
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	return response

def votee(request, mashov_id):
    mmashov = get_object_or_404(mashov, pk=mashov_id)
    try:
        selected_choice = request.GET["vote"]
    except (KeyError, mashov.DoesNotExist):
        return render(request, 'mashovvote.html', {
            'mashov': mmashov,
            'error_message': "You didn't select a choice.",
        })
    else:
    	mmashov.feedback += int(selected_choice)
    	if(selected_choice == "10"):
		    mmashov.v1 += 1
    	elif(selected_choice == "30"):
    		mmashov.v2 +=1
    	elif(selected_choice == "60"):
    		mmashov.v3 +=1
    	elif(selected_choice == "80"):
    		mmashov.v4 +=1
    	elif(selected_choice == "100"):
    		mmashov.v5 +=1
    	mmashov.save()
    	return render(request,"kidsPage.html")

def reviews(request,Review_id):
	reviews_list = Review.objects.order_by('-id')[:20]
	context = {'reviews_list': reviews_list}
	return render(request, "ReviewsKids.html", context)