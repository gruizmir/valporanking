# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from main.models import Article
from main.forms import RankForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

@csrf_exempt
def rank(request):
    if request.method == "POST":
        form = RankForm(request.POST)
        print request.POST
        if form.is_valid():
            fb_shared = form.cleaned_data['facebook_share']
            tw_shared = form.cleaned_data['twitter_share']
            name = form.cleaned_data['name']
            try:
                art = Article.objects.get(name=name)
            except:
                art = Article()
                art.name = name
                art.save()
                
            if fb_shared:
                art.facebook_count = art.facebook_count + 1
                art.facebook_rate = (art.facebook_rate + form.cleaned_data['facebook_rate'])/art.facebook_count
                art.save()
            elif tw_shared:
                art.twitter_count = art.twitter_count + 1
                art.twitter_rate = (art.twitter_rate + form.cleaned_data['twitter_rate'])/art.twitter_count
                art.save()
            else:
                return HttpResponse("ERROR NOT SHARED")
            return HttpResponse("OK")
        else:
            return HttpResponse("ERROR NOT VALID")
    else:
        #~ rForm = RankForm()
        #~ return render_to_response("input.html", {'form':rForm}, context_instance=RequestContext(request))
        return HttpResponse("ERROR METHOD")
