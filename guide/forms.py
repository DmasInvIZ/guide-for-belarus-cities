from django import forms
from guide.models import UserTowns


# форма отправки публикации админу
class SuggestForm(forms.ModelForm):

    class Meta:
        model = UserTowns
        fields = ['town', 'watch', 'eat', 'sleep']
