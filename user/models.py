from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user.personal_info.models import PersonalInfo

from user.managers import UserManager

def avatar_directory_path(instance, filename):
    return 'user/{1}/avatar/{1}'.format(instance.username, filename)


class User(AbstractBaseUser):
    password = models.CharField(max_length=128) #здесь можно было не задавать пароль. если пользователь через др почтой тогда null=True,например когда заходим через google 
    is_active = models.BooleanField(default=True) # по умолчанию пользователь стразу становится активный т.к в этом приложении не будем пользоваться почтой итд. в коммерческих проектах сначала фолс если пользователь подтверждает через почту итд становится тру
    username = models.EmailField(max_length=70, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False, help_text='admin') # когда создаем суперпользователья default=True будет
    avatar = models.ImageField(upload_to=avatar_directory_path, null=True, blank=True) #null=True это значит пользователь может не загр аватар
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, null=True, related_name='user')


    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []    # при создании пользователья обязательные поля


    def check_is_admin(self, request=None):
        return self.is_staff # and request.url not in '/financial_report'

    # user.get_full_name = user = related_name
    def get_full_name(self):
        return '{0} {1} {2}'.format(self.personal_info.last_name, self.personal_info.first_name, self.personal_info.middle_name)    


    def __str__(self):
        return self.username
