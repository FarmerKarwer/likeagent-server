from django.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
	name = models.CharField(max_length=70)
	preview_image = models.ImageField(upload_to = 'uploads/')
	brief_description = models.TextField(max_length=350)
	main_description = models.TextField(max_length=1500)
	number_of_questions = models.PositiveSmallIntegerField()

	def __str__(self):
		return f"{self.name}"

	def get_questions(self):
		return self.question_set.all()[:self.number_of_questions]

	def get_resultgroups(self):
		return self.resultgroup_set.all()

	class Meta:
		verbose_name_plural = 'Quizes'

class ResultGroup(models.Model):
	group_name = models.CharField(max_length=200)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

	def __str__(self):
		return f"name: {self.group_name}, quiz: {self.quiz.name}"

class Question(models.Model):
	text = models.CharField(max_length=200)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	result_group = models.ForeignKey(ResultGroup, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.text)

	def get_answers(self):
		return self.answer_set.all()

class Answer(models.Model):
	text = models.CharField(max_length=200)
	score = models.IntegerField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return f"question: {self.question.text}, answer: {self.text}, score: {self.score}"

class Result(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	text = models.TextField(max_length=1500)
	result_group = models.ForeignKey(ResultGroup, on_delete=models.CASCADE, null=True)		

class Condition(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField(max_length=1500)
	min_score = models.IntegerField()
	max_score = models.IntegerField()
	result = models.ForeignKey(Result, on_delete=models.CASCADE)

class UserResult(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	test_result = models.JSONField(null=True)