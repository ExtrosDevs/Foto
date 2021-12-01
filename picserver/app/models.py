from django.db import models
from datetime import datetime
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ManyToManyField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.fields.json import JSONField

# from django.contrib.postgres.fields import ArrayField
# from django.db.models.expressions import F
from django_countries.fields import CountryField


# Create your models here.
class User(models.Model):
    choices = (
        ('user', 'user'),
        ('premium', 'premium'),
        ('superuser', 'superuser')
    )
    userName = models.CharField(max_length=30, unique=True)
    firstName = models.CharField(max_length=30, default='unknown')
    lastName = models.CharField(max_length=30,default='unknown')
    birthDate = models.DateField(null=True)
    pic  = models.ImageField(upload_to="userPic",default="default.jpg")
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=180)
    userPermissions  = models.CharField(max_length=30,choices=choices, default='user')
    userstatus = models.BooleanField(default=False)
    bio = models.TextField(blank=True,null=True)
    country = CountryField(blank=True,null=True)
    pointes = models.IntegerField(default=0)
    # favorite = models.ManyToManyField('Image')
    following = models.ManyToManyField('self',blank=True,null=True)
    chats = models.ManyToManyField('Chat',blank=True,null=True)


    tagsLike = models.ManyToManyField('Tag',blank=True,null=True)

    createdDate = models.DateTimeField(default=datetime.now())
    emailActvate =models.BooleanField(default=False)
    def __str__(self):
        return f"{self.userName}"



class Tag(models.Model):
    tagName = CharField(default='ss', max_length=30)
    def __str__(self):
        return f"{self.tagName}"

class Image(models.Model):
    
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    # m = models.ManyToManyField(User)
    imageTitle = models.CharField(max_length=60, default="unknown")

    image = models.ImageField(upload_to='publicImages',default="default.jpg")
    imageDesc = models.CharField(max_length=300, default='')
    tags = models.ManyToManyField(Tag,blank=True,null=True)
    # genre = models.CharField(max_length=30, choices= choices)
    
    imageDate = models.DateField(default=datetime.now())
    likes = models.IntegerField(default=0 )
    usernameLikes = models.JSONField(default=[{}])
    private = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.imageTitle[:15]}   ,{self.id}"


class ChatImage(models.Model):
    image = models.ImageField(upload_to='chatImages',default="default.jpg")
    user =models.ForeignKey(User, on_delete=models.CASCADE)
class Chat(models.Model):
    users = models.ManyToManyField(User)    
    chat = models.JSONField(default=[{}])

    