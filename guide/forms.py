from django import forms
from guide.models import UserTowns


class SuggestForm(forms.ModelForm):
    """Форма отправки публикаций в админку"""

    class Meta:
        model = UserTowns
        fields = ['town', 'watch', 'eat', 'sleep']
