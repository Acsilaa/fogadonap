from django.shortcuts import render
from django.http import HttpResponse 
from ..models import Teacher

# Create your views here.
def index(req):

    teachers = Teacher.objects.all()

    return render(req, 'index.html', {"data":teachers})

def login(req):
    return HttpResponse(render(req, "header.html")) + HttpResponse(render(req, "login.html")) + HttpResponse(render(req, "footer.html"))
