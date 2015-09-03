from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile
from .forms import ProfileForm
#Register your models here.

from django.contrib.auth.models import Permission

class UserInline(admin.ModelAdmin):
	model = Userprofile	
	def get_form(self, request, obj=None, **kwargs):
		if not request.user.is_superuser:
			return ProfileForm

	def get_queryset(self, request):
		result = super(UserInline, self).get_queryset(request)
		if not request.user.is_superuser:
			return result.filter(user=request.user.id)
		return result
		

admin.site.register(Userprofile,UserInline)