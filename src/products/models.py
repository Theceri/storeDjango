from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils.six.moves.urllib.parse import (
    quote, quote_plus, unquote, unquote_plus, urlencode as original_urlencode,
    urlparse,
)
from django.contrib.auth.models import User
from userprofile.models import Userprofile
# Create your models here.

CATEGORY_CHOICES = (
		('electronics','electronics'),
		('fashion','fashion'),
	)

class Products(models.Model):
	name = models.CharField(max_length=150,blank=False,null=False)
	price = models.CharField(max_length=150,blank=False,null=False)
	category = models.CharField(max_length=150,choices=CATEGORY_CHOICES,blank=False,null=False)
	photo = models.FileField(upload_to='puloads/%Y/%m/%d')
	owner = models.ForeignKey(User)
	description = models.TextField(max_length=1000,blank=False,null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('view', kwargs={'name':quote_plus(self.name),'id':self.id})

