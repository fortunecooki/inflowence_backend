# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    def __str__(self):
        return self.content

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()