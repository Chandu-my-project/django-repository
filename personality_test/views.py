from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def personality_test(request):
    return render(request,'personality_test/ptest.html',{})

def prec(request):
    all_points = student_points.objects.all()
    list1=[]
    final_score={}

    if request.method == "POST":
        all_personality = personality.objects.all()
        rdes=personality.objects.filter(personality_type="Realistic")
        ides=personality.objects.filter(personality_type="Investigative")
        ades = personality.objects.filter(personality_type="Artistic")
        sdes = personality.objects.filter(personality_type="Social")
        edes = personality.objects.filter(personality_type="Enterprising")
        cdes = personality.objects.filter(personality_type="Conventional")
        if request.POST.get('points'):
            user_points = request.POST.get('points')
            point = user_points.split(",")
            for i in range(len(all_points)):
                all_points[i].points = point[i]
                all_points[i].save()
        realistic=['R1','R2','R3','R4','R5']
        robj=[]
        rpoints=[]
        for item in realistic:
            robj.append(student_points.objects.filter(personality_number=item))
        for obj in robj:
            rpoints.append(obj[0].points)
        rtot=sum(rpoints)
        rper=round(float((rtot/20)*100))

        investigative=['I1','I2','I3','I4','I5']
        iobj=[]
        ipoints=[]
        for item in investigative:
            iobj.append(student_points.objects.filter(personality_number=item))
        for obj in iobj:
            ipoints.append(obj[0].points)
        itot=sum(ipoints)
        iper=round(float((itot/20)*100))

        artistic=['A1','A2','A3','A4','A5']
        aobj=[]
        apoints=[]
        for item in artistic:
            aobj.append(student_points.objects.filter(personality_number=item))
        for obj in aobj:
            apoints.append(obj[0].points)
        atot=sum(apoints)
        aper=round(float((atot/20)*100))

        social=['S1','S2','S3','S4','S5']
        sobj=[]
        spoints=[]
        for item in social:
            sobj.append(student_points.objects.filter(personality_number=item))
        for obj in sobj:
            spoints.append(obj[0].points)
        stot=sum(spoints)
        sper=round(float((stot/20)*100))

        enterprising=['E1','E2','E3','E4','E5']
        eobj=[]
        epoints=[]
        for item in enterprising:
            eobj.append(student_points.objects.filter(personality_number=item))
        for obj in eobj:
            epoints.append(obj[0].points)
        etot=sum(epoints)
        eper=round(float((etot/20)*100))

        conventional = ['C1', 'C2', 'C3', 'C4', 'C5']
        cobj = []
        cpoints = []
        for item in conventional:
            cobj.append(student_points.objects.filter(personality_number=item))
        for obj in cobj:
            cpoints.append(obj[0].points)
        ctot = sum(cpoints)
        cper = round(float((ctot / 20) * 100))
        ######MAIN LOGIC ########
        list1.append(rper)
        final_score['R']=rper
        list1.append(iper)
        final_score['I'] = iper
        list1.append(aper)
        final_score['A'] = aper
        list1.append(sper)
        final_score['S'] = sper
        list1.append(eper)
        final_score['E'] = eper
        list1.append(cper)
        final_score['C'] = cper
        sorted_values = sorted(final_score.values(), reverse=True)
        sorted_dict = {}
        for i in sorted_values:
            for k in final_score.keys():
                if final_score[k] == i:
                    sorted_dict[k] = final_score[k]
        N = 3
        out = dict(list(sorted_dict.items())[0: N])
        per = list(out.keys())
        print(per)
        order=list(sorted_dict.keys())
        print(order)
        # Function to convert
        def listToString(s):

            # initialize an empty string
            str1 = ""

            # traverse in the string
            for ele in s:
                str1 += ele

                # return string
            return str1

        combo=listToString(per)
        ######END OF LOGIC ########
        obj1=''
        obj2=''
        obj3=''
        for i in range(len(per)):
            if i == 0:
                obj1=personality_cluster.objects.filter(personality=per[0])

            elif i==1:
                obj2=personality_cluster.objects.filter(personality=per[1])
            elif i==2:
                obj3 = personality_cluster.objects.filter(personality=per[2])
            else:
                continue

        print(obj1)
        print(obj2)
        print(obj3)


        common1=obj1.filter(career_cluster__in=obj2.values_list('career_cluster',flat=True))
        common2=obj2.filter(career_cluster__in=obj3.values_list('career_cluster',flat=True))
        common3 = obj3.filter(career_cluster__in=obj1.values_list('career_cluster', flat=True))
        common_items=common1.filter(career_cluster__in=obj3.values_list('career_cluster', flat=True))
        # while final1!=final2!=final3!=final4:
        final1 = obj1[0]
        final2 = obj1[1]
        final3 = obj2[0]
        final4 = obj3[0]
        # if common_items.exists():
        #     final1 = common_items.first()
        # else:
        #     final1 = obj1[2]
        #
        # if common1.exists():
        #     final2=common1.first()
        # else:
        #     final2=obj1[1]
        #
        # if common2.exists():
        #     final3=common2.first()
        # else:
        #     final3 = obj2[3]
        #
        # if common3.exists():
        #     final4=common3.first()
        # else:
        #     final4 = obj3[4]


        # if final1!=None and final2!=None and final3!=None and final4!=None:
        #     if final1==final2:
        #         final2=obj1[2]
        #     elif final1==final3:
        #         final3 = obj2[1]
        #     elif final1==final4:
        #         final4=obj3[1]
        #     elif final2==final3:
        #         final3=obj2[2]
        #     elif final2==final4:
        #         final4=obj3[2]
        #     elif final3==final4:
        #         final4=obj3[3]
        #     else:
        #         pass
        # else:
        #     pass
        final1_des = cluster.objects.filter(cluster_name=final1)
    return render(request,'personality_test/prec.html',{'all_points':all_points,'rper':rper,'iper':iper,'aper':aper,'sper':sper,'eper':eper,'cper':cper,'combo':combo,'final1':final1,'final2':final2,'final3':final3,'final4':final4,'obj1':obj1,'final1_des':final1_des,'order':order,'rdes':rdes,'ides':ides,'ades':ades,'sdes':sdes,'edes':edes,'cdes':cdes})

def cluster_info(request,cluster_id):
    image=cluster.objects.all()
    cf=get_object_or_404(cluster,pk=cluster_id)
    cm=cluster_major.objects.filter(career_cluster=cluster_id)
    return render(request,'personality_test/c_info.html',{'cf':cf,'cm':cm,'image':image})

def start_test(request):
    return render(request,'personality_test/s_ptest.html',{})