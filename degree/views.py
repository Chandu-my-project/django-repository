from django.shortcuts import render, get_object_or_404
from .models import *


def search_deg(request):
    dis=Discipline.objects.all()
    return render(request,'degree/discipline.html',{'dis':dis})

def info(request,discipline_id):
    dis=get_object_or_404(Discipline,pk=discipline_id)
    return  render(request,'degree/info.html',{'dis':dis})