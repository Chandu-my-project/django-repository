from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage

def quiz(request):
    all_questions = Quiz.objects.all()
    p = Paginator(all_questions, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)

    return render(request, 'quiz/index.html', {"all_questions": all_questions})


def rec(request):
    user = request.user
    all_questions = Quiz.objects.all()
    if request.method == "POST":
        if request.POST.get('coursename'):
            schoice = request.POST.get('coursename')
            print(schoice)
            qchoice = schoice.split(",")
            for i in range(len(all_questions)):
                all_questions[i].selected_ans = qchoice[i]
                all_questions[i].save()
        subjects = {}
        objects = {}
        score = {}
        answers = {}
        sel_answers = {}
        totals = {}
        degree = {}
        final = {}
        for s in Subject.objects.all():
            subjects[s.sub_name] = s.id
        for sub, sub_id in subjects.items():
            objects[sub] = Quiz.objects.filter(subject=sub_id)
            degree[sub] = Degree.objects.filter(subject=sub_id)
        for sub, obj in objects.items():
            temp1 = []
            temp2 = []
            points = 0
            totals[sub] = len(obj)
            for item in obj:
                temp1.append(item.answer)
                temp2.append(item.selected_ans)
                if item.answer == item.selected_ans:
                    points += 1
                else:
                    points += 0
            answers[sub] = temp1
            sel_answers[sub] = temp2
            score[sub] = points
        # If they score full marks
        for sub in subjects:
            if totals[sub] == score[sub]:
                final[sub] = degree[sub]
            else:
                continue
        # Highest marks
        v = list(score.values())
        k = list(score.keys())
        high = max(v)
        num_of_high = v.count(high)

        # Suppose they got same marks in all subject
        # if num_of_high==1:
        #     msub = k[v.index(max(v))]
        #     final[msub] = degree[msub]
        # else:
        if high == 0:
            None
        else:
            ans = [k for k, v in score.items() if v == high]
            for item in ans:
                final[item] = degree[item]
        sub1_obj = Subject.objects.get(pk=1)
        sub2_obj = Subject.objects.get(pk=2)
        sub3_obj = Subject.objects.get(pk=3)
        sub4_obj = Subject.objects.get(pk=4)
        sub5_obj = Subject.objects.get(pk=5)
        if 'Arts, Design & Architecture' in final.keys():
            # obj,created = Recommendation.objects.get_or_create(subject=sub1_obj, tot_score=5, marks=4,rec='True',user_name="Vbhj")
            obj1 = Recommendation(subject=sub1_obj, tot_score=totals['Arts, Design & Architecture'], marks=score['Arts, Design & Architecture'], rec='True',
                                  user_name=user.username)
            obj1.save()
        else:
            pass

        if 'Computer Science & IT' in final.keys():
            # obj,created = Recommendation.objects.get_or_create(subject=sub1_obj, tot_score=5, marks=4,rec='True',user_name="Vbhj")
            obj2 = Recommendation(subject=sub2_obj, tot_score=totals['Computer Science & IT'], marks=score['Computer Science & IT'], rec='True',
                                  user_name=user.username)
            obj2.save()
        else:
            pass
        if 'Natural Sciences & Mathematics' in final.keys():
            # obj,created = Recommendation.objects.get_or_create(subject=sub1_obj, tot_score=5, marks=4,rec='True',user_name="Vbhj")
            obj3 = Recommendation(subject=sub3_obj, tot_score=totals['Natural Sciences & Mathematics'], marks=score['Natural Sciences & Mathematics'], rec='True',
                                  user_name=user.username)
            obj3.save()
        else:
            pass
        if 'Business & Management' in final.keys():
            # obj,created = Recommendation.objects.get_or_create(subject=sub1_obj, tot_score=5, marks=4,rec='True',user_name="Vbhj")
            obj4 = Recommendation(subject=sub4_obj, tot_score=totals['Business & Management'], marks=score['Business & Management'], rec='True',
                                  user_name=user.username)
            obj4.save()
        else:
            pass
        if 'Humanities' in final.keys():
            # obj,created = Recommendation.objects.get_or_create(subject=sub1_obj, tot_score=5, marks=4,rec='True',user_name="Vbhj")
            obj5 = Recommendation(subject=sub5_obj, tot_score=totals['Humanities'],
                                  marks=score['Humanities'], rec='True',
                                  user_name=user.username)
            obj5.save()
        else:
            pass

    return render(request, 'quiz/rec.html',
                  {"all_questions": all_questions, "answers": answers, "score": score, "sel_answers": sel_answers,
                   "final": final, "totals": totals,'sub1_obj':sub1_obj,'sub2_obj':sub2_obj,'sub3_obj':sub3_obj,'sub4_obj':sub4_obj,'sub5_obj':sub5_obj})


def start_quiz(request):
    user = request.user

    obj = Recommendation.objects.all()
    user_name_list = []
    final_list = []
    if obj:
        for item in obj:
            user_name_list.append(getattr(item, 'user_name'))

        for item in user_name_list:
            if item in final_list:
                continue
            else:
                final_list.append(item)

        for name in final_list:
            if name == user.username:
                return render(request, 'quiz/attain.html', {})
            else:
                continue
        return render(request, 'quiz/squiz.html', {})

    else:
        return render(request, 'quiz/squiz.html', {})


def attained(request):
    return render(request, 'quiz/attain.html', {})


def view_rec(request):
    user = request.user
    user_rec = Recommendation.objects.filter(user_name=user.username)
    sub1_obj = Subject.objects.get(pk=1)
    sub2_obj = Subject.objects.get(pk=2)
    sub3_obj = Subject.objects.get(pk=3)
    sub4_obj = Subject.objects.get(pk=4)
    sub5_obj = Subject.objects.get(pk=5)
    score_list = []
    tot_score_list = []
    subject_list = []
    subject_obj_list = []
    subject_id_list = []
    deg_obj = {}
    final = {}
    per_list=[]
    per_dic = {}
    for item in user_rec:
        score_list.append(getattr(item, 'marks'))
        tot_score_list.append(getattr(item, 'tot_score'))
        subject_list.append(str(getattr(item, 'subject')))
    for item in score_list:
        val=int(item)
        per=round(int((val/3)*100))
        per_list.append(per)
    for key in subject_list:
        for value in per_list:
            per_dic[key] = value
            break
    if 'Arts, Design & Architecture' not in per_dic:
        per_dic['Arts, Design & Architecture'] = 0
    else:
        pass
    if 'Computer Science & IT' not in per_dic:
        per_dic['Computer Science & IT'] = 0
    else:
        pass
    if 'Natural Sciences & Mathematics' not in per_dic:
        per_dic['Natural Sciences & Mathematics'] = 0
    else:
        pass
    if 'Business & Management' not in per_dic:
        per_dic['Business & Management'] = 0
    else:
        pass
    if 'Humanities' not in per_dic:
        per_dic['Humanities'] = 0
    else:
        pass

    for sub in subject_list:
        subject_obj_list.append(Subject.objects.get(sub_name=sub))
    for item in subject_obj_list:
        subject_id_list.append(getattr(item, 'pk'))

    sub_id_dict = {subject_list[i]: subject_id_list[i] for i in range(len(subject_list))}

    for sub, sub_id in sub_id_dict.items():
        deg_obj[sub] = Degree.objects.filter(subject=sub_id)

    for sub, obj in deg_obj.items():
        temp1 = []
        for item in obj:
            temp1.append(item.deg_name)
        final[sub] = temp1

    return render(request, 'quiz/view_rec.html',
                  {'tot_score_list': tot_score_list, 'score_list': score_list, 'subject_list': subject_list,
                   'final': final,'user_rec':user_rec,'sub1_obj':sub1_obj,'sub2_obj':sub2_obj,'sub3_obj':sub3_obj,'sub4_obj':sub4_obj,'sub5_obj':sub5_obj,'per_dic':per_dic})


def pagination(request):
    all_questions = Quiz.objects.all()
    p=Paginator(all_questions,5)
    print("number of pages")
    print(p.num_pages)
    page_num=request.GET.get('page',1)
    try:

        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)

    return render(request,'quiz/page.html',{'all_questions':page})