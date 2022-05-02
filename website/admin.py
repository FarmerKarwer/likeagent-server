from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Quiz)
admin.site.register(ResultGroup)
admin.site.register(UserResult)
class AnswerInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

class ConditionInline(admin.TabularInline):
	model = Condition

class ResultAdmin(admin.ModelAdmin):
	inlines = [ConditionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)