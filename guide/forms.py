from ckeditor.widgets import CKEditorWidget
from django import forms
from guide.models import UserTowns


# форма отправки публикации админу
class SuggestForm(forms.ModelForm):
    # watch = forms.CharField(widget=CKEditorWidget(), label='')

    class Meta:
        model = UserTowns
        fields = ['town', 'watch', 'eat', 'sleep']
