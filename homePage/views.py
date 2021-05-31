from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache

@never_cache
def login_success(request):
    if request.user.groups.filter(name="Parents").exists():
        return redirect("parentsPage")
    elif request.user.groups.filter(name="Kids").exists():
        return redirect("kidsPage")
    elif request.user.is_superuser:
        return redirect("/ganenet")
	
def logout_view(request):
    logout(request)	

def about(request):
    return render(request,"about.html")
	
