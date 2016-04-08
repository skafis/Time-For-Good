from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Person(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=100)
	


	def __unicode__(self):
		return self.name
		
# models for creating opportunity
class Create_opportunity(models.Model):
    title = models.CharField(max_length=140)
    location = models.CharField(max_length=140)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
