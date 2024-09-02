from django.contrib import admin
#from . import models
from tweetapp.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group',{'fields':["message"]}),
        ('Nickname Group',{'fields':["nickname"]}),
    ]
    #fields = ['nickname', 'message'] #hangisini onceden yaptiginiz onemli





# Register your models here.
admin.site.register(Tweet,TweetAdmin)