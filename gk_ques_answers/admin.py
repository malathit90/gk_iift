from django.contrib import admin
from gk_ques_answers.models import questions, question_type

class gk_questions_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Question Details', {'fields' : ['question', 'answer', 'type']}),
        ('Additional Description', {'fields' : ['answer_description']}),
    ]
    list_display = ('question', 'answer', 'type')
    search_fields = ('question', 'answer')
    list_filter = ('type', 'time_added')

admin.site.register(questions, gk_questions_Admin)
admin.site.register(question_type)