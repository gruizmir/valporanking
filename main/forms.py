# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm, Form, BooleanField, CharField, IntegerField
from main.models import *


class RankForm(Form):
    name = CharField(required=True, label="Nombre")
    smw_id = IntegerField(required=False, label="ID wiki")
    facebook_share = BooleanField(required=False, label="Nota facebook")
    twitter_share = BooleanField(required=False, label="Nota twitter")
    facebook_rate = IntegerField(required=False, label="Nota facebook")
    twitter_rate = IntegerField(required=False, label="Nota twitter")


class ImgForm(ModelForm):
    class Meta:
        model = Imagen
        exclude = ('votes',)


class VoteImageForm(Form):
    name = CharField(required=True, label="Nombre")
    img_id = IntegerField(required=True, label="ID imagen")
