from django.db import models
from article.models import Article 


class AddComment(models.Model):
    author_name = models.CharField('Name', max_length=50, null=True, blank=True)
    comment_text = models.CharField('Comment', max_length=300)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') #'article.Article'
    create_date = models.DateTimeField('Created date', auto_now_add=True)


    class Meta:
        ordering = ['-create_date']


    # def __str__(self):
    #     return 'Comment added by {} at {}'.format(self.name, self.create_date)    

    # article_id = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='comments') #'article.Article'
    # article_id = models.ManyToManyField(Article, on_delete=models.CASCADE, related_name='comments') #'article.Article'
