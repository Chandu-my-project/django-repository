from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.db import transaction
from .models import User, Student, Teacher


level_choices=[("puc","PUC Student"),("under graduate","Under Graduate Student")]
major_choices=[("science","Science"),("commerce","Commerce"),("arts","Arts")]
combo_choices1=[("P.C.M.B","P.C.M.B"),("P.C.M.E","P.C.M.E"),("P.C.M.C"," P.C.M.C"),("P.C.M.G"," P.C.M.G"),("P.C.B.H","P.C.B.H"),("P.C.B.E"," P.C.B.E")]
combo_choices=[("P.C.M.B","P.C.M.B"),("P.C.M.E","P.C.M.E"),]
combo_choices2=[("SEBA","SEBA"),("ABEM","ABEM"),("BSAM","BSAM"),("EBAC","EBAC"),("HEBA","HEBA"),("GEBA","GEBA"),("BACS","BACS"),("ABPE","ABPE")]
combo_choices3=[("HEGP","HEGP"),("HEPK","HEPK"),("HEGK","HEGK"),("HEEduP","HEEduP"),("HEKM","HEKM")]
status_choices=[("Currently a student","Currently a student"),("passed out","Passed out student"),("No longer a student","No longer a student")]

class dob(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="First name")
    last_name = forms.CharField(required=True,label="Last name")
    phone_number = forms.CharField(required=True,label="Phone Number")
    edu_level=forms.CharField(required=True,label="Education Level",widget=forms.Select(choices=level_choices))
    # status=forms.CharField(required=True,label="Education Status",widget=forms.Select(choices=status_choices))
    grad_year = forms.IntegerField(required=True,label="Graduation year")
    college_name = forms.CharField(required=True, label="College/University name")
    email = forms.CharField(required=True, label="College mail ID")
    # major=forms.CharField(label="Major Subject",widget=forms.Select(choices=major_choices))
    # combo1 = forms.CharField(label="Subject Combination", widget=forms.Select(choices=combo_choices1))
    # combo2 = forms.CharField(label="",widget=forms.Select(choices=combo_choices2))
    # combo3 = forms.CharField(label="", widget=forms.Select(choices=combo_choices3))

    class Meta(UserCreationForm.Meta):
        model = User



    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.edu_level = self.cleaned_data.get('edu_level')
        user.grad_year = self.cleaned_data.get('grad_year')
        user.college_name=self.cleaned_data.get('college_name')
        # user.major = self.cleaned_data.get('major')
        # user.combo = self.cleaned_data.get('combo1')
        # user.combo = self.cleaned_data.get('combo2')
        # user.combo = self.cleaned_data.get('combo3')
        # user.status = self.cleaned_data.get('status')
        user.is_active = False
        user.save()

        student = Student.objects.create(user=user)
        student.phone_number = self.cleaned_data.get('phone_number')
        student.email = self.cleaned_data.get('email')
        student.edu_level = self.cleaned_data.get('edu_level')
        student.grad_year = self.cleaned_data.get('grad_year')
        student.college_name=self.cleaned_data.get('college_name')
        # student.major = self.cleaned_data.get('major')
        # student.combo = self.cleaned_data.get('combo1')
        # student.combo = self.cleaned_data.get('combo2')
        # student.combo = self.cleaned_data.get('combo3')
        # student.status = self.cleaned_data.get('status')
        student.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    college_name = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.college_name = self.cleaned_data.get('college_name')
        teacher.save()
        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),label="Email")
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label="First Name")
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label="Last Name")
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label="User Name")
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),label="Phone Number")
    edu_level = forms.CharField(required=True, label="Education Level", widget=forms.Select(choices=level_choices))
    grad_year = forms.IntegerField(required=True, label="Graduation year")
    # dob = forms.DateField(widget=dob, required=True, label="Date of birth")
    college_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),label="College Name")
    # major = forms.CharField(required=True, label="Major Subject", widget=forms.Select(choices=major_choices))
    # combo = forms.CharField(required=True, label="Subject Combination", widget=forms.Select(choices=combo_choices))
    password = None
    class Meta():
        model = User
        fields=('username','first_name','last_name','college_name','email','phone_number','edu_level','grad_year')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}),label="Old Password")
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label="New Password")
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label="Confirm New Password")

    class Meta():
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')