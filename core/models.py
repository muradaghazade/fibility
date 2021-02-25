from django.db import models


class AboutUsText(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'About us text'
        verbose_name_plural = 'About us texts'

class MoreOnUsText(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'More on us text'
        verbose_name_plural = 'More on us texts'