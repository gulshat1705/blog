from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from article.models import Article
from comment.models import AddComment
from comment.forms import FormCreateForm 


# Create your views here.
def comment(request, id):
    article_obj = Article.objects.get(id=id)
    form = FormCreateForm()
    context = {'article': article_obj, 'comment_form': form}

    
    if request.method == 'POST':
        form = FormCreateForm(request.POST)
        if form.is_valid():
            comment_obj = AddComment(author_name=form.cleaned_data['author_name'], 
            comment_text=form.cleaned_data['comment_text'], article=article_obj)
            comment_obj.save()
        else:
            return render(request, 'comment.html', context)              
    comment_obj = AddComment.objects.filter(article = article_obj)
    comment_counts = comment_obj.count()

    return render(request, 'comment.html', {'article': article_obj, 'form': form, 'comments': comment_obj, 'comment_counts': comment_counts})

    # article_obj = Article.objects.get(id=id)
    # form = FormCreateForm()

    # context = {'article': article_obj, 'comment_form': form}

    # if request.method == 'GET':
    
    #     return render(request, 'comment.html', context)
    # else:
    #     form = FormCreateForm(request.POST)
    #     if form.is_valid():
    #         comments = AddComment.objects.filter(article__id = id)
    #         comment_obj = AddComment(name=form.cleaned_data['author_name'], 
    #         text=form.cleaned_data['comment_text'], article=article_obj)
    #         comment_obj.save()
    #         # return redirect('home')  
    #         return render(request, 'comment.html', context)              