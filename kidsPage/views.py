from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from homePage.models import subject

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,"kidsPage.html")
	
def contents(request, subject_id):
	data = subject.objects.all()
	sub = {
    "subject_id": data
	}
	return render(request,"subject.html", sub)
	
def download_file(request,fl_path):
	data = subject.objects.all()
	sub = {
    "subject_id": data
	}
	fl_path = data.values('submissions')[0]['submissions']
	filename = fl_path.split('/')[1]
	fl = open(fl_path, 'r')
	response = HttpResponse(fl, content_type='application/pdf')
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	return response	

def Meetings(request):
    return render(request, "Meetings.html")