from django.db import models
# from django.core.validators import validators
#create table about
class About(models.Model):
    email = models.CharField(("email"), max_length=50)
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=100) 
    message = models.CharField('message', max_length=300)
    allow_mailing = models.BooleanField(default=False)    