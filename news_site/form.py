from django import forms

from .models import NewsModel


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['news_title', 'news_categories', 'news_tags', 'news_news', 'news_image',
                  'news_author']


class SearchForm(forms.Form):
    search_bar = forms.CharField(max_length=256)

