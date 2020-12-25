from django.db import models
from accounts.models impor CustomUser as User
from home.models import Category
# Create your models here.
class Skill(models.Model):
    title=models.CharField('Title',max_length=150,)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


class Service(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField('Title',max_length=150,)
    description=models.CharField('Description', max_length=500)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.FileField()
    skill=models.ForeignKey(Skill,on_delete=models.CASCADE)
    is_published= models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Pocket(models.Model):
    title=models.CharField('Title',max_length=150,)
    description=models.CharField('Description', max_length=500)
    service=models.ForeignKey(Service,on_delete=models.CASCADE,releated_name='pockets')
    cost=models.IntegerField(min_value=1, max_value=10000)

    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title
    
