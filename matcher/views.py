from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Candidate, Job
from .serializers import CandidateSerializer, JobSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @action(['GET'], False)
    def candidates_finder(self, request):
        job_title = request.query_params.get('job')
        if not job_title:
            return Response(data='Please provide a job title', status=status.HTTP_400_BAD_REQUEST)
        filtered_jobs = self.queryset.filter(title__icontains=job_title)
        if not filtered_jobs.exists():
            return Response(data=f'No candidates found for {job_title} job.', status=status.HTTP_200_OK)
        required_skills = filtered_jobs.values_list('skills', flat=True).distinct()
        candidates = Candidate.objects.filter(skills__in=required_skills).distinct()
        return Response(CandidateSerializer(candidates, many=True).data)
