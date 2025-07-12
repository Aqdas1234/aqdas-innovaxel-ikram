from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShortURLSerializer
from rest_framework.generics import RetrieveAPIView
from .models import ShortURL
from django.shortcuts import get_object_or_404


class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.save()  
            return Response(ShortURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortURLDetailView(RetrieveAPIView):
    def get(self, request, shortCode):
        short_url = get_object_or_404(ShortURL, shortCode=shortCode)
        serializer = ShortURLSerializer(short_url)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ShortURLUpdateView(APIView):
    def put(self, request, shortCode):
        short_url = get_object_or_404(ShortURL, shortCode=shortCode)
        serializer = ShortURLSerializer(short_url, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)