from django import forms
from comment.models import AddComment


class FormCreateForm(forms.ModelForm):
    class Meta:
        model = AddComment
        fields =  ('author_name', 'comment_text')
        # exclude = ['create_date']

        