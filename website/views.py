from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def login_view(request, *args, **kwargs):
	return render(request, "auth.html", {})

def tests(request, *args, **kwargs):
	return render(request, "tests.html", {})

def tests_swl(request, *args, **kwargs):
	context = {
	"title" : "Удовлетворенность жизнью"
	}
	return render(request, "swl.html", context)

def tests_big5(request, *args, **kwargs):
	context = {
	"title" : "Big Five"
	}
	return render(request, "big five.html", context)

def tests_temper(request, *args, **kwargs):
	context = {
	"title" : "Темперамент"
	}
	return render(request, "temper.html", context)

def tests_typeofthinking(request, *args, **kwargs):
	context = {
	"title" : "Тип мышления"
	}
	return render(request, "type_of_thinking.html", context)

# Getting social code
def get_social_code(request):
	print(request.GET['code'])