from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .filters import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
def search_inst(request):

    deg_institute = DegreeInstitution.objects.all()
    myFilter = DegreeInstitutionFilter(request.GET, queryset=deg_institute)
    deg_institute=myFilter.qs
    return render(request,'search/isearch.html',{'deg_institute':deg_institute,'myFilter':myFilter})
    # return HttpResponse("<h1>hello</h1>")

def favorite(request,institute_id):
    user=request.user
    pname=user.username
    degree = get_object_or_404(DegreeInstitution, pk=institute_id)
    #deg_institute = DegreeInstitution.objects.all()
    try:
        if degree.is_favorite:
            degree.is_favorite = False
        else:
            degree.is_favorite = True
        degree.person_name = pname
        degree.save()
    except (KeyError, degree.DoesNotExist):
        #return JsonResponse({'success': False})
        messages.error(request,'Not Added to your Institution Shortlist!!')
        return redirect('/search/')
    else:
        #return JsonResponse({'success': True})
        messages.success(request, 'Added to your Institution Shortlist!!')
        return redirect('/search/')

def interested(request):
    user = request.user
    pname = user.username
    user_interest=DegreeInstitution.objects.filter(person_name=pname)
    return render(request,'search/interest.html',{'user_interest':user_interest})

def deleteOrder(request,pk):
    order = DegreeInstitution.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/search/interested/')
    context={'item':order}
    return render(request,'search/delete.html',context)
