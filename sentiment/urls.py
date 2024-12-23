from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'sentiment'
urlpatterns = [
    # /sentiment/
    path('', views.index, name="index"),

    # /sentiment/<institute_id>/
    url(r'^(?P<institute_id>[0-9]+)/$', views.detail, name="detail"),

    # /sentiment/<institute_id>/<course_id>/
    url(r'^(?P<institute_id>[0-9]+)/(?P<course_id>[0-9]+)/$', views.fb, name="fb"),

    path('review/', views.review, name="review"),

    # /sentiment/<institute_id>/favorite/
    # url(r'^(?P<institute_id>[0-9]+)/favorite/$', views.favorite, name="favorite")
    path('review_error/', views.review_error, name="review_error"),
    path('review_submit/', views.review_submit, name="review_submit"),


]
