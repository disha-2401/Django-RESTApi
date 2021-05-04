from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=200,primary_key=True)
    completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    pages = models.IntegerField(max_length=10000)

    def __str__(self):
        return self.title


class BTSMembers(models.Model):
    Member_Choices = (
        ('RM', 'NamJoon'),
        ('jin', 'SeokJin'),
        ('Suga', 'Yoongi'),
        ('J-Hope', 'HoSeok'),
        ('jimin', 'Jimin'),
        ('V', 'Tae'),
        ('JungKook', 'JungKook'),
    )
    MemberName = models.CharField(max_length=8,choices=Member_Choices,default='jimin')
    age = models.IntegerField()
    GoodThingAboutHim = models.CharField(max_length=100)

    def __str__(self):
        return self.MemberName