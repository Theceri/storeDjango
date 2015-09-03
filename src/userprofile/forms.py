from django.template import RequestContext
from django import forms
from django import forms
from .models import Userprofile
from django.forms.extras.widgets import SelectDateWidget
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = ['email','location','yourlogo','description','is_active']