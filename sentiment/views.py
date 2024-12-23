# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from django.core.files import File
import string
from django.db.models import Sum
from collections import Counter
import matplotlib.pyplot as plt
import random
import os

def index(request):
    all_institute = Institutes.objects.all()
    # template=loader.get_template('sentiment/index.html')
    # Information my template needs its dictionary
    context = {'all_institute': all_institute}
    # return HttpResponse(template.render(context,request))
    # httpresponse is behind the scene in render ,it converts to httpresponse
    return render(request, 'sentiment/index.html', context)


def detail(request, institute_id):
    # try:
    #     institute=Institutes.objects.get(pk=institute_id)
    # except Institutes.DoesNotExist:
    #     raise Http404("Institute does not exist")
    # shortcut for try and except
    institute = get_object_or_404(Institutes, pk=institute_id)
    return render(request, 'sentiment/detail.html', {'institute': institute})


def fb(request, course_id, institute_id):
    template_name = 'sentiment/fb.html'
    comments = get_object_or_404(Course, pk=course_id)

    # tot_stars = Feedback.objects.filter(course=course_id).aggregate(Sum('rating'))
    count = Feedback.objects.filter(course=course_id).count()
    # val_stars = tot_stars.values()
    # for val in val_stars:
    #     ov_rating = 0
    #     if isinstance(val, int) == True:
    #         tot = sum(val_stars)
    #         ov_rating = round(tot / count)
    #     else:
    #         continue
    # comments.overall_rating = ov_rating
    # comments.save()
    return render(request, template_name,
                  {'comments': comments, "count": count})


def favorite(request, institute_id):
    institute = get_object_or_404(Institutes, pk=institute_id)
    try:
        # it tooks the value from detail form that is nothing but the course id which we selected
        selected_course = institute.course_set.get(pk=request.POST['course'])
    except(KeyError, Course.DoesNotExist):
        return render(request, 'sentiment/detail.html', {
            'institute': institute,
            'error_message': "You did not select a valid course"})
    else:
        selected_course.is_favorite = True
        selected_course.save()
        return render(request, 'sentiment/detail.html', {'institute': institute})


def review(request):
    user = request.user
    uname = user.username
    template_name = 'sentiment/review.html'
    path = "C://final_project/final_website/sentiment/emotions.txt"
    final_words = []
    emotion_list = []

    if request.method == 'POST':
        inst_value1 = ''
        deg_value1 = ''
        inst_value2 = ''
        deg_value2 = ''
        # Comment posted
        obj = Feedback.objects.filter(pname=uname)
        iname_list=[]
        dname_list=[]
        if obj is not None:
            for item in obj:
                inst=str(getattr(item, 'deg_inst'))
                course=str(getattr(item,'course'))
                if inst not in iname_list and course not in dname_list:
                    iname_list.append(inst)
                    dname_list.append(course)
                else:
                    pass
        else:
            pass
        sel_inst = request.POST.get('deg_inst')
        sel_deg = request.POST.get('course')
        inst_obj = Institutes.objects.filter(pk=sel_inst).first()
        deg_obj = Course.objects.filter(pk=sel_deg).first()
        if inst_obj is not None and deg_obj is not None:
            inst_value2 = str(getattr(inst_obj, 'iname'))
            deg_value2 = str(getattr(deg_obj, 'cname'))
        else:
            pass
        if len(iname_list) is not 0:
            for iname in iname_list:
                if iname==inst_value2:
                    inst_value1+=iname
                else:
                    pass
        else:
            pass
        if len(dname_list) is not 0:
            for dname in dname_list:
                if dname==deg_value2:
                    deg_value1+=dname
                else:
                    pass
        else:
            pass

        if inst_value1 == inst_value2 and deg_value1 == deg_value2:
            return redirect('/sentiment/review_error/')
        else:
            form = model_form(request.POST or None, request.FILES or None)
            if form.is_valid():
                new_comment = form.save(commit=False)
                rate1 = request.POST.get('star1')
                rate2 = request.POST.get('star2')
                rate3 = request.POST.get('star3')
                orate = request.POST.get('star')
                new_comment.rating = int(orate)
                new_comment.star1 = int(rate1)
                new_comment.star2 = int(rate2)
                new_comment.star3 = int(rate3)
                tot_rate = round((int(rate1) + int(rate2) + int(rate3) + int(orate)) / 4)
                new_comment.tot_rating = int(tot_rate)
                new_comment.pname = user.username
                text = new_comment.review
                lower_case = text.lower()
                cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
                score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)


                # Sentiments of the comments
                if score['neg'] > score['pos']:
                    new_comment.sentiment = "Negative Review"

                elif score['neg'] < score['pos']:
                    new_comment.sentiment = "Positive Review"
                else:
                    new_comment.sentiment = "Neutral Review"

                new_comment.save()
            #overal rating
            sel_course = request.POST.get('course')
            comments = get_object_or_404(Course, pk=sel_course)
            tot_stars = Feedback.objects.filter(course=sel_course).aggregate(Sum('tot_rating'))
            count = Feedback.objects.filter(course=sel_course).count()
            val_stars = tot_stars.values()
            for val in val_stars:
                ov_rating = 0
                if isinstance(val, int) == True:
                    tot = sum(val_stars)
                    ov_rating = round(tot / count)
                else:
                    None
            comments.overall_rating = ov_rating

            #count of pos,neg and neu
            reviews = Feedback.objects.filter(course=sel_course)
            sent_list = []
            pos_rev=0
            neg_rev=0
            neu_rev=0
            for item in reviews:
                sent_list.append(getattr(item, 'sentiment'))
            for item in sent_list:
                if item=="Positive Review":
                    pos_rev+=1
                elif item=="Negative Review":
                    neg_rev+=1
                else:
                    neu_rev+=1
            comments.pos=pos_rev
            comments.neg=neg_rev
            comments.neu=neu_rev
            comments.save()
            return redirect('/sentiment/review_submit/')

    form = model_form()
    return render(request, template_name, {'form': form})


def review_error(request):
    return render(request, 'sentiment/review_error.html', {})


def review_submit(request):
    return render(request, 'sentiment/review_submit.html', {})
