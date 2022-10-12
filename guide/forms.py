from ckeditor.widgets import CKEditorWidget
from django import forms
from guide.models import UserTowns


class SuggestForm(forms.ModelForm):

    class Meta:
        model = UserTowns
        fields = ['author', 'town', 'district', 'watch', 'eat', 'sleep']
