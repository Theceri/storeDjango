from django.contrib import admin

# Register your models here.
from .models import Products
from .forms import ProductForm

class ProductsAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","id","price","category","photo"]
	form = ProductForm

	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()

	def get_queryset(self, request):
		qs = super(ProductsAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(owner=request.user)


admin.site.register(Products,ProductsAdmin)
