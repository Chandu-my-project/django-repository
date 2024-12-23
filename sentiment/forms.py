from django import  forms
from .models import *
DEGREE_CHOICES = (
    ('Bachelor Degree','Bachelor Degree'),
    ('Associate Degree', 'Associate Degree'),
    ("Master's Degree","Master's Degree"),
    ('Doctoral Degree','Doctoral Degree'),
)

STATUS_CHOICES = (
    ('Currently attending','Currently attending'),
    ('Graduated', 'Graduated'),
    ("No longer attending","No longer attending"),
)

CLASS_CHOICES = (
    ('Online','Online'),
    ('On Campus', 'On Campus'),
    ("Hybrid/Both","Hybrid/Both"),
)

class model_form(forms.ModelForm):
    #deg_inst = forms.CharField(label="College/Institution",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    #course = forms.CharField(label="Major",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    # deg_inst = forms.Select(required=True, label="Degree Institution")
    deg_level = forms.CharField(required=True, label="Degree Level", widget=forms.Select(choices=DEGREE_CHOICES))
    enroll_status = forms.CharField(required=True, label="Enrollment Status", widget=forms.Select(choices=STATUS_CHOICES))
    grad_year = forms.IntegerField(required=True, label="Graduation year")
    class_env = forms.CharField(required=True, label="Class environment", widget=forms.Select(choices=CLASS_CHOICES))

    class Meta:
        model=Feedback
        fields=['deg_inst','course','deg_level','enroll_status','grad_year','class_env','review']


# class model_form(forms.ModelForm):
#     class Meta:
#         model=rev
#         fields=['review']