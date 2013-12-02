# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from main.models import Article
from main.forms import RankForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import render_to_response

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
        #~ form = RankForm()
        #~ return render_to_response("input.html", {'form':form}, context_instance=RequestContext(request))
        return HttpResponse("ERROR METHOD")

@csrf_exempt
def best(request):
    if request.method == "POST":
        if 'cant' in request.POST:
            cant = request.POST.get('cant')
        else:
            cant = 5
        data = serializers.serialize('json', Article.objects.all().order_by('total_count')[:cant],
            fields=('name', 'total_count', 'facebook_count', 'twitter_count'))
        print data
        return HttpResponse(data, mimetype='application/json')    
    else:
        return HttpResponse("ERROR METHOD")

@csrf_exempt
def worst(request):
    if request.method == "POST":
        if 'cant' in request.POST:
            cant = request.POST.get('cant')
        else:
            cant = 5
        data = serializers.serialize('json', Article.objects.all().order_by('-total_count')[:cant],
            fields=('name', 'total_count', 'facebook_count', 'twitter_count'))
        return HttpResponse(data, mimetype='application/json')    
    else:
        return HttpResponse("ERROR METHOD")    
    
