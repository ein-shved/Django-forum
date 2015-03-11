import datetime
from django.db import models
from django.utils import timezone
from django.contrib import auth

class Topic(models.Model):
    publisher = models.ForeignKey(auth.models.User)
    topic_header = models.CharField(max_length = 256)
    topic_text = models.CharField(max_length = 2048)

class Reply(models.Model):
    topic = models.ForeignKey(Topic)
    publisher = models.ForeignKey(auth.models.User)
    reply_text = models.CharField(max_length = 512)

