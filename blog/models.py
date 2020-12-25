from django.db import models

# Create your models here.

class Service(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField('Title',max_length=150,)
    description=models.CharField('Description', max_length=500)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    is_published= models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Pocket(models.Model):
    title=models.CharField('Title',max_length=150,)
    description=models.CharField('Description', max_length=500)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    cost=models.IntegerField(min_value=1, max_value=10000)
    
    def __str__(self):
        return self.title