from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShortURLSerializer

class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.save()  
            return Response(ShortURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
