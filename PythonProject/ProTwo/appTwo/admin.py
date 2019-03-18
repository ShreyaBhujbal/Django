from django.contrib import admin
from appTwo.models import Branch, AdmissionStats, Question, Choice
# Register your models here.

admin.site.register(Branch)
admin.site.register(AdmissionStats)
admin.site.register(Question)
admin.site.register(Choice)
