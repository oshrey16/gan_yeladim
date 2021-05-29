from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from homePage.models import mashov, subject, Meeting
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def index(request):
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

def vote(request, mashov_id):
    ssubject = get_object_or_404(subject, pk=mashov_id)
    try:
        selected_choice = ssubject.choice_set.get(pk=request.POST['mashov'])
    except (KeyError, mashov.DoesNotExist):
        return render(request, 'mashovvote.html', {
            'mashov': ssubject,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(ssubject.id,)))

