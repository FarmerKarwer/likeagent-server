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
def privacy_policy_view(request):
	return render(request, "privacy_policy.html", {})

@method_decorator(login_required(login_url='/accounts/vk/login/'), name='dispatch')
class QuizListView(ListView):
	model = Quiz
	template_name = 'index.html'

@method_decorator(login_required(login_url='/accounts/vk/login/'), name='dispatch')
class TestListView(ListView):
	model = Quiz
	template_name = 'tests.html'


@login_required(login_url='/accounts/vk/login/')
def quiz_view(request, pk):
	quiz = Quiz.objects.get(pk=pk)
	return render(request, 'tests/base_test.html', {'obj' : quiz})

@login_required(login_url='/accounts/vk/login/')
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

@login_required(login_url='/accounts/vk/login/')
def additional_data_view(request, pk):
	questions_list = AdditionalQuestion.objects.all()
	questions = []
	for q in questions_list:
		answers = []
		for a in q.get_answers():
			answers.append(a.answer)
		questions.append({str(q): answers})
	return JsonResponse({
		'data' : questions,
		})

@login_required(login_url='/accounts/vk/login/')
def save_additional_data_view(request, pk):
	if is_ajax(request):
		data = request.POST
		data_ = dict(data.lists())
		data_.pop('csrfmiddlewaretoken')
		if all(value == [''] for value in data_.values())==False:
			user = request.user
			UserAdditionalResult.objects.create(user=user, info=data_)

	return JsonResponse({'text': 'additional_data_view'})

@login_required(login_url='/accounts/vk/login/')
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

		user_result_dict = {}
		result_dict = {}

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

			for r in group_results:
				result_conditions = Condition.objects.filter(result=r)
				cond_results = {}
				for c in result_conditions:
					if c.min_score <= score <= c.max_score:
						cond_results.update({"name":c.name, "score": score, "text": c.text,  "description" : r.text})
			result_dict.update({group.group_name:cond_results})
			user_result_dict.update({group.group_name:cond_results["name"]})
		
		UserResult.objects.create(quiz=quiz, user=user, test_result=user_result_dict)

	return JsonResponse(result_dict)