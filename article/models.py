from django.db import models
from datetime import datetime


def article_directory_path(instance, filename):
    return 'article/{0}/{1}'.format(datetime.today().strftime('%d-%m-%Y'), filename)


class Article(models.Model):
    title = models.CharField('Title', max_length=100)
    short_description = models.CharField('Short Description', max_length=300, null=True)
    description = models.TextField('Text')
    image = models.ImageField('Image', upload_to=article_directory_path, null=True)
    created_date = models.DateTimeField('Created date', auto_now_add=True)
    updated_date = models.DateTimeField('Updated date', auto_now=True)    



    
# Create your models here.

