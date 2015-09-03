from django.shortcuts import render

# Create your views here.
def about(request):
	context = {
		'title': "About Us",
		'description':'About Xuwon.com'
	}
	return render(request, "aboutus.html", context)

def contact(request):
	context = {
		'title': "About Us",
		'description':'contact Xuwon.com'
	}
	return render(request, "contact.html", context)

def services(request):
	context = {
		'title': "About Us",
		'description':'services Xuwon.com'
	}
	return render(request, "services.html", context)