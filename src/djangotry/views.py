from django.contrib.sitemaps import Sitemap
from products.models import Products
import datetime

class PSitemap(Sitemap):
	changefeg = "daily"
	priority = 0.5
	lastmod = datetime.datetime.now()

	def items(self):
		return Products.objects.all()

	