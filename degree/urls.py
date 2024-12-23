from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'degree'
urlpatterns = [
    path('', views.search_deg, name='search_deg'),
    url(r'^(?P<discipline_id>[0-9]+)/$',views.info,name="info"),

]
