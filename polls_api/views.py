from django.http import request
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Poll
from election_api.models import Election
from election_api.serializers import ElectionSerializer, TypeSerializer
from candidate_api.models import Candidate
from candidate_api.serializers import CandidateSerializer
from .serializers import PollSerializer, PollResultSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
class ListCreatePollView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class DetailCreatePollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class Result(APIView):

    def get(self, request, candidate_id):
        candidates = Candidate.objects.filter(id=candidate_id).all()
        candidate_ser = CandidateSerializer(candidates, many=True)
        
        if len(candidate_ser.data) == 0:
            data = {
                "status": "error", 
                "message": "Invalid candidate"
            }
            return Response(data)

        
        election = Election.objects.filter(id=1).all()
        serializer = ElectionSerializer(election, many=True)

        results =  Poll.objects.filter(candidate_id=candidate_id).count()
        data = {
            "total_votes": results,
            "candidate": candidate_ser.data[0],
            "election": serializer.data[0]
        }

        return Response(data)

class GeneralResult(APIView):
    def get(self, request):

        final_results = []
        candidates = Candidate.objects.filter(election_id=1)
        candidate_ser = CandidateSerializer(candidates, many=True)

        
        if len(candidate_ser.data) == 0:
            data = {
                "status": "error", 
                "message": "Invalid candidate"
            }
            return Response(candidate_ser.data)


        for i in candidate_ser.data:
            candidate_id = i['id']
            candidates = Candidate.objects.filter(id=candidate_id).all()
            candidate_ser = CandidateSerializer(candidates, many=True)
            
            election = Election.objects.filter(id=1).all()
            serializer = ElectionSerializer(election, many=True)

            results =  Poll.objects.filter(candidate_id=candidate_id).count()

            data = {
                "total_votes": results,
                "candidate": candidate_ser.data[0],
                "election": serializer.data[0]
            }

            final_results.append(data)

        return Response(final_results)
        
             




