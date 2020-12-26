from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField('Category',max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


