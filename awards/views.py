from django.shortcuts import render
from django.http import HttpResponse
from .models import  Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-posted_on')
    form = DesignForm()
    form = UsabilityForm()
    form = ContentForm()
    return render(request, 'index.html', locals())

