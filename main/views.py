# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from main.models import Article
from main.forms import RankForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.utils import simplejson

@csrf_exempt
def rank(request):
    if request.method == "POST":
        form = RankForm(request.POST)
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
                art.total_count = art.total_count + 1
                art.facebook_rate = (art.facebook_rate + form.cleaned_data['facebook_rate'])/art.facebook_count
                art.save()
            elif tw_shared:
                art.twitter_count = art.twitter_count + 1
                art.total_count = art.total_count + 1
                art.twitter_rate = (art.twitter_rate + form.cleaned_data['twitter_rate'])/art.twitter_count
                art.save()
            else:
                return HttpResponse("ERROR NOT SHARED")
            return HttpResponse("OK")
        else:
            return HttpResponse("ERROR NOT VALID")
    else:
        return HttpResponse("ERROR METHOD")


def best(request):
    if request.method == "POST":
        if 'cant' in request.POST:
            cant = request.POST.get('cant')
        else:
            cant = 5
        art = Article.objects.all().order_by('total_count')[:cant]
        data = model_to_dict(art, fields=['name', 'total_count'], exclude=['facebook_count', 'twitter_count', 'twitter_rate', 'facebook_rate', 'smw_id'])
        json = simplejson.dumps(data)
        return HttpResponse(json, mimetype='application/json')    
    else:
        return HttpResponse("ERROR METHOD")


def hipster(request):
    if request.method == "POST":
        if 'cant' in request.POST:
            cant = request.POST.get('cant')
        else:
            cant = 5
        art = Article.objects.all().order_by('total_count')[:cant]
        data = model_to_dict(art, fields=['name', 'total_count'], exclude=['facebook_count', 'twitter_count', 'twitter_rate', 'facebook_rate', 'smw_id'])
        json = simplejson.dumps(data)
        return HttpResponse(json, mimetype='application/json')    
    else:
        return HttpResponse("ERROR METHOD")    
    
