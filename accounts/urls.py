from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'acc'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('teacher_register/', views.teacher_register.as_view(), name='teacher_register'),
    path('login/', views.login_request, name='login'),
    path('shome/', views.shome, name='shome'),
    path('logout/', views.logout_view, name='logout'),
    path('student_edit/', views.student_edit.as_view(), name='student_edit'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change-password.html'),name='password_change'),
    path('password_success/', views.password_success, name='password_success'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name="activate"),
    path('sample/',views.sample,name="sample"),


]
