from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# admin.site.register(Question) # old way of adding question to admin

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)