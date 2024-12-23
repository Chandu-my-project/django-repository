from django.urls import path, include
from . import views

app_name = 'quiz'
urlpatterns = [

    path('', views.quiz, name='quiz'),
    path('rec/', views.rec, name="rec"),
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('view_rec/', views.view_rec, name='view_rec'),
    path('attained/', views.attained, name='attained'),
    path('page/',views.pagination, name='pagination'),
    # path('', include('django.contrib.auth.urls'))
]
