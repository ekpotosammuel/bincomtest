from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class CandidateAPIView(APIView):
    
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetails(APIView):
    def get_obeject(self, id):
        try:
            return Candidate.objects.get(id=id)

        except Candidate.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        candidate = self.get_obeject(id)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, id):
        candidate = self.get_obeject(id)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        candidate = self.get_obeject(id)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
