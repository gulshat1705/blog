from django import forms
from article.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exlude = ('created_date', 'updated_date')