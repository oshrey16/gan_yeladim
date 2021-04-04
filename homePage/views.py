from django.http import HttpResponse
from django.shortcuts import redirect

#def index(request):
 #   return HttpResponse("Hello. This is our home page! WELCOME!")
	


def login_success(request):
    if request.user.groups.filter(name="Parents").exists():
        return redirect("parentsPage")
    elif request.user.groups.filter(name="Kids").exists():
        return redirect("kidsPage")
    elif request.user.is_superuser:
        return redirect("/ganenet")
	