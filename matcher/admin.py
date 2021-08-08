from django.contrib import admin
from .models import Candidate, Skill, Job


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
