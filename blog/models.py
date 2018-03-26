# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post (models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	author = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

