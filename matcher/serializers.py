from rest_framework.serializers import ModelSerializer

from .models import Candidate, Job, Skill


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

