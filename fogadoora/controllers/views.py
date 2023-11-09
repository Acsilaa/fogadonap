from django.shortcuts import render
from ..models import Teacher

# Create your views here.
def index(req):

    teachers = Teacher.objects.all()

    return render(req, 'index.html', {"data":teachers})