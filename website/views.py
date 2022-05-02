from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required(login_url='/accounts/vk/login/'), name='dispatch')
class QuizListView(ListView):
	model = Quiz
	template_name = 'index.html'

@login_required(login_url='/accounts/vk/login/')
def tests(request, *args, **kwargs):
	return render(request, "tests.html", {})
@login_required(login_url='/accounts/vk/login/')
def tests_swl(request, *args, **kwargs):
	context = {
	"title" : "Удовлетворенность жизнью"
	}
	return render(request, "swl.html", context)
@login_required(login_url='/accounts/vk/login/')
def tests_big5(request, *args, **kwargs):
	context = {
	"title" : "Big Five"
	}
	return render(request, "big five.html", context)
@login_required(login_url='/accounts/vk/login/')
def tests_temper(request, *args, **kwargs):
	context = {
	"title" : "Темперамент"
	}
	return render(request, "temper.html", context)
@login_required(login_url='/accounts/vk/login/')
def tests_typeofthinking(request, *args, **kwargs):
	context = {
	"title" : "Тип мышления"
	}
	return render(request, "type_of_thinking.html", context)




def quiz_view(request, pk):
	quiz = Quiz.objects.get(pk=pk)
	return render(request, 'tests/base_test.html', {'obj' : quiz})