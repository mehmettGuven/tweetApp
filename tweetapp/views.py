from django.shortcuts import render,redirect
from . import models
from django.urls import reverse

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request,'tweetapp/listtweet.html',context=tweet_dict)

def addtweet(request):
    if request.POST:
        nickname =request.POST['nickname']
        message =  request.POST['message']
        models.Tweet.objects.create(nickname=nickname, message=message)
        '''
        tweet = models.Tweet(nickname,message)
        tweet.save()
        '''
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request,'tweetapp/addtweet.html')