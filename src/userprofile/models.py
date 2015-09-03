from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	joined = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(max_length='150')
	location = models.CharField(max_length='150')
	yourlogo = models.FileField(upload_to='logos/%Y/%m/%d',blank=True)
	description = models.TextField(max_length='1000')
	is_active = models.BooleanField(default=True)
	is_verified = models.BooleanField(default=True)

	USERNAME_FIELD = 'username'

	def __unicode__(self):
		return self.email;
