from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import StudentSignUpForm, TeacherSignUpForm,EditProfileForm,PasswordChangingForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import *
from .utils import token_generator
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from django.core.mail import EmailMessage
from django.urls import reverse
from quiz.models import Recommendation
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

def register(request):
    return render(request,'accounts/register.html')



class student_register(CreateView):
    model = User
    form_class =  StudentSignUpForm
    template_name = 'accounts/student_register.html'

    def form_valid(self, form):
        user = form.save()
        email_id = user.email
        email_subject = 'Activate your account'
        uidb64=urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(self.request).domain
        #link=reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
        link='/accounts/activate/'+uidb64+'/'+token_generator.make_token(user)
        activate_url='http://'+domain+link
        email_body = 'Hi '+user.username+',\nPlease use this link to verify your account\n'+activate_url
        email = EmailMessage(
            email_subject,
            email_body,
            'chandu2181999@gmail.com',
            [email_id],

        )
        email.send(fail_silently=False)
        user.is_active = True
        user.save()
        login(self.request, user)
        messages.success(self.request, 'Account successfully created!!')
        return redirect('/accounts/student_register/')



class teacher_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/teacher_register.html'



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/login/')





def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_student==True:
                    return redirect('/accounts/shome/')
                else:
                    return redirect('/')
            else:

                messages.error(request,"Invalid username or password")
        else:
             messages.error(request,"Invalid username or password")

    return render(request, 'accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

class student_edit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'
    #appname:url folders name of the function
    #success_url = reverse_lazy("acc:student_edit")

    def get_success_url(self):
        messages.success(self.request, 'Profile Updated Successfully.')
        return reverse("acc:student_edit")

    def get_object(self):
        return self.request.user




def shome(request):

    return render(request, 'accounts/shome.html',{})

class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('acc:password_success')
    def get_success_url(self):
        messages.success(self.request, 'Password Updated Successfully.')
        return reverse("acc:password_change")


def password_success(request):
    return render(request,'accounts/password_success.html',{})

class VerificationView(View):
    def get(self,request,uidb64,token):
        return redirect('/accounts/login/')

def sample(request):
    return render(request, 'accounts/sample.html',{})