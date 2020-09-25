from django import forms
from django.db.models import fields

from courses.models import Review
# from models import UserProfile
# from django.froms.widgets import RadioSelect


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('deviceNb',)

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('student', 'lesson', 'text')
