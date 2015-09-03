
try:
	from .local import *
except Exception, e:
	pass

try:
	from .production import *
except Exception, e:
	pass