from django.shortcuts import render
from django.http import HttpResponse
from .models import Election, Type
from .serializers import ElectionSerializer, TypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class ElectionAPIView(APIView):
    
    def get(self, request):
        elections = Election.objects.all()
        serializer = ElectionSerializer(elections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ElectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ElectionDetails(APIView):
    def get_obeject(self, id):
        try:
            return Election.objects.get(id=id)

        except Election.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        election = self.get_obeject(id)
        serializer = ElectionSerializer(election)
        return Response(serializer.data)

    def put(self, request, id):
        election = self.get_obeject(id)
        serializer = ElectionSerializer(election, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        election = self.get_obeject(id)
        election.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Election Type
class TypeAPIView(APIView):
    
    def get(self, request):
        elections = Type.objects.all()
        serializer = TypeSerializer(elections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TypeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDetails(APIView):
    def get_obeject(self, id):
        try:
            return Type.objects.get(id=id)

        except Type.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        election = self.get_obeject(id)
        serializer = TypeSerializer(election)
        return Response(serializer.data)

    def put(self, request, id):
        election = self.get_obeject(id)
        serializer = TypeSerializer(election, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        election = self.get_obeject(id)
        election.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)