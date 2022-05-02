from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import HttpResponse


def is_ajax(request):
  return request.headers.get('x-requested-with') == 'XMLHttpRequest'

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


def quiz_data_view(request, pk):
	quiz = Quiz.objects.get(pk=pk)
	questions = []
	for q in quiz.get_questions():
		answers = []
		for a in q.get_answers():
			answers.append(a.text)
		questions.append({str(q): answers})
	return JsonResponse({
		'data' : questions,
		})

def save_quiz_view(request, pk):
	if is_ajax(request):
		questions = []
		data = request.POST
		data_ = dict(data.lists())
		
		data_.pop('csrfmiddlewaretoken')

		for k in data_.keys():
			question = Question.objects.get(text = k)
			questions.append(question)

		user = request.user
		quiz = Quiz.objects.get(pk=pk)
		result_groups = list(Quiz(pk=pk).get_resultgroups())

		for group in result_groups:
			group_questions = Question.objects.filter(result_group=group)
			group_results = Result.objects.filter(result_group=group)
			score = 0

			for q in group_questions:
				a_selected = request.POST.get(q.text)

				if a_selected != "":
					question_answers = Answer.objects.filter(question=q)
					for a in question_answers:
						if a_selected == a.text:
							score+=a.score
			results = []
			for r in group_results:
				result_conditions = Condition.objects.filter(result=r)
				cond_results = []
				for c in result_conditions:
					if c.min_score <= score <= c.max_score:
						cond_results.append({"name":c.name, "text": c.text})
				results.append({"condition": cond_results, "score": score, "description" : r.text})
			print(results)

	return JsonResponse({'text': 'works'})