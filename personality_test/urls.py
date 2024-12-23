from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'ptest'
urlpatterns = [
    path('', views.personality_test, name='personality_test'),
    path('start_test/', views.start_test, name='start_test'),
    path('prec/', views.prec, name="prec"),
    url(r'^(?P<cluster_id>[0-9]+)/$',views.cluster_info,name="cluster_info"),

]
