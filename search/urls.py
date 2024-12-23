from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.search_inst, name='search_inst'),
    # /search/<institute_id>/favorite/
    url(r'^(?P<institute_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
    # path('favorite/', views.favorite, name="favorite"),
    path('interested/', views.interested, name="interested"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
