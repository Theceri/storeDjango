import datetime
from haystack import indexes
from .models import Products

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	pub_date = indexes.DateTimeField(model_attr='timestamp')
	content_auto = indexes.EdgeNgramField(model_attr = 'name')

	def get_model(self):
		return Products
	def index_queryset(self, using=None):
		return self.get_model().objects.all()

