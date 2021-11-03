from django.shortcuts import render
from article.models import Article 
# from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    articles = Article.objects.all().order_by('-created_date')
    paginator = Paginator(articles, 2)

    page_number = request.GET.get('page') 
    try:
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)    # если ключа нет деф зн 1
    except EmptyPage:
        page = paginator.page(paginator.num_pages)    

    return render(request, 'index.html', {'page': page})
    
# def index(request, page=1):
    # items_per_page = 10
    # offset = items_per_page * (page-1)
    # articles = Article.objects.all().order_by('-created_date')
    # articles_count = articles.count()
    # pages_range = range(1, int(math.ceil(articles_count / items_per_page) + 1))
    # return render(request, 'index.html', {'title': 'Home', 'articles': articles[offset: items_per_page * page], 
    # 'articles_count': articles_count, 'pages_range': pages_range})

def article_new(request, id):
    article_obj= Article.objects.get(id=id)
    context = {'id': article_obj}
    return render(request, 'article-new.html', context)  
