import django_filters
from .models import *
from django.forms.widgets import TextInput
from django_filters import CharFilter, RangeFilter

field_value3 = []
field_name3 = 'Degree_Course'
obj3 = DegreeInstitution.objects.all()
for item3 in obj3:
    field_value3.append(getattr(item3, field_name3))
# print(field_value)
final_course = []
for course in field_value3:
    if course == '─':
        None
    elif course in final_course:
        None
    else:
        final_course.append(course)
# print(final_fees)
COURSE_CHOICES = ()
for item3 in final_course:
    temp3 = ()
    for i in range(0, 2):
        temp3 = temp3 + (item3,)
    # print(temp)
    COURSE_CHOICES = COURSE_CHOICES + (temp3,)
# print(COURSE_CHOICES)

# state

field_value2 = []
field_name2 = 'State'
obj2 = DegreeInstitution.objects.all()
for item2 in obj2:
    field_value2.append(getattr(item2, field_name2))
# print(field_value)
final_state = []
for state in field_value2:
    if state == '─':
        None
    elif state in final_state:
        None
    else:
        final_state.append(state)
# print(final_fees)
STATE_CHOICES = ()
for item2 in final_state:
    temp2 = ()
    for i in range(0, 2):
        temp2 = temp2 + (item2,)
    # print(temp)
    STATE_CHOICES = STATE_CHOICES + (temp2,)
# print(STATE_CHOICES)

# fees
field_value = []
field_name = 'Total_Fees'
obj = DegreeInstitution.objects.all()
for item in obj:
    field_value.append(getattr(item, field_name))
# print(field_value)
final_fees = []
for fee in field_value:
    if fee == '─':
        None
    elif fee in final_fees:
        None
    else:
        final_fees.append(fee)
# print(final_fees)
FEES_CHOICES = ()
for item in final_fees:
    temp = ()
    for i in range(0, 2):
        temp = temp + (item,)
    # print(temp)
    FEES_CHOICES = FEES_CHOICES + (temp,)
# print(FEES_CHOICES)

# ranking

field_value1 = []
field_name1 = 'Ranked'
obj1 = DegreeInstitution.objects.all()
for item1 in obj1:
    field_value1.append(getattr(item1, field_name1))
# print(field_value)
final_rank = []
for rank in field_value1:
    if rank == '─':
        None
    elif rank in final_rank:
        None
    else:
        final_rank.append(rank)
# print(final_fees)
RANK_CHOICES = ()
for item1 in final_rank:
    temp1 = ()
    for i in range(0, 2):
        temp1 = temp1 + (item1,)
    # print(temp)
    RANK_CHOICES = RANK_CHOICES + (temp1,)


# print(RANK_CHOICES)
class DegreeInstitutionFilter(django_filters.FilterSet):
    State = django_filters.ChoiceFilter(choices=STATE_CHOICES, label="State")
    Degree_Course = django_filters.ChoiceFilter(choices=COURSE_CHOICES, label="Degree Course")
    Total_Fees = django_filters.ChoiceFilter(choices=FEES_CHOICES, label="Total Fees")
    Ranked = django_filters.ChoiceFilter(choices=RANK_CHOICES, label="Ranking")
    Institute_name = django_filters.CharFilter(field_name="Institute_name", lookup_expr='icontains',
                                               label='Institution name',
                                               widget=TextInput(attrs={'placeholder': 'Enter the Institution name'}))

    class Meta:
        model = DegreeInstitution
        fields = ['State','Degree_Course','Total_Fees','Ranked','Institute_name']
        exclude = ['Location', 'is_favorite', 'person_name']
