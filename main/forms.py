from django.db.models import fields
from django.forms import ModelForm
from main import models

class CreatePollForm(ModelForm):
    class Meta:
        model = models.Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']
