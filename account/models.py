from django.db import models
from django.contrib.auth.models import AbstractUser
from .common import slugify
from django.core.mail import send_mail

class User(AbstractUser):
    email = models.EmailField(('email adress'), unique=True, null=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    is_employed = models.BooleanField(default=False)
    occupation = models.CharField(max_length=255, null=True)
    salary = models.IntegerField(null=True)
    number = models.CharField(max_length=100, null=True)
    # company = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='images')
    is_advisor = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.username)}'
        super(User, self).save(*args, **kwargs)

class Message(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='message')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='themessage')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.subject}'

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        print(self.subject, self.text, self.sender.email, self.receiver.email)
        send_mail(self.subject, f'from {self.sender.email} \n {self.text}', self.sender.email, [self.receiver.email,])
        super(Message, self).save(*args, **kwargs)

# class Region(models.Model):
#     title = models.CharField(max_length=255, null=True)
#     added_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.title}'

#     class Meta:
#         verbose_name = 'Region'
#         verbose_name_plural = 'Regions'

# class TypeOfAdvice(models.Model):
#     title = models.CharField(max_length=255, null=True)
#     added_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.title}'

#     class Meta:
#         verbose_name = 'Type of Advice'
#         verbose_name_plural = 'Types of Advices'