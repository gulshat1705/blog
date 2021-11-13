from django.http.response import Http404
from django.shortcuts import render
from article.forms import ArticleCreateForm
from django.contrib import messages

# from django.core.exceptions import ValidationError
# from blog.article.models import Article
# from article.models import article
# from comment.forms import CommentForm
# 

def create(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            article_form = ArticleCreateForm(request.POST, request.FILES)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, 'Your post was created!')        

            else:
                return render(request, 'article.html', {'form': article_form, 'error': article_form.errors})  
    else:
        raise Http404         

    form = ArticleCreateForm()  
    return render(request, "article.html", {'form': form})


# Create your views here.
