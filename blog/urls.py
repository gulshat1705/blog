from django.contrib import admin
from django.urls import path
from main.views import index
from about.views import about
from comment.views import comment
from article.views import create
from django.conf.urls.static import static
from blog import settings

# from catapp.views import form_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'), 
    path('<int:page>', index, name='home'),
    path('comment/<int:id>/', comment, name='comments'),
    path('article', create, name='create'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)