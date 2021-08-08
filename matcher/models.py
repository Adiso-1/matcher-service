from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, default=None, unique=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    title = models.CharField(max_length=255, default=None)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None, unique=True)
    mobile = models.CharField(max_length=255, default=None, unique=True)
    skills = models.ManyToManyField(to='Skill', blank=True, default=None)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Job(models.Model):
    title = models.CharField(max_length=255, null=False, default=None, unique=True)
    skills = models.ManyToManyField(to='Skill', default=None, blank=True)

    def __str__(self):
        return self.title
