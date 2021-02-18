from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(('email adress'), unique=True, null=True)
    full_name = models.CharField(max_length=100)
    # region
    age = models.IntegerField(null=True)
    is_employed = models.BooleanField(default=False)
    occupation = models.CharField(max_length=255, null=True)
    salary = models.IntegerField(null=True)
    number = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='images')
    is_advisor = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)
    # type of advice


    # user_type = models.ManyToManyField('UserType', verbose_name=("User Type"))
    # slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     self.slug = f'{slugify(self.username)}'
    #     super(User, self).save(*args, **kwargs)
