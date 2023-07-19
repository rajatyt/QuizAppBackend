from django.contrib import admin
from .models import Updated,Quizzes,Question,Category,Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_right']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','date_created']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','quiz','technique','title','difficulty','date_created','is_active']
    inlines = [AnswerInline,]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','question','answer_text','is_right']





