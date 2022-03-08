from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django.core.exceptions import ObjectDoesNotExist

from .serializers import AdditionSerializer
from .models import Addition


#for class based view
from rest_framework.views import APIView

#logging the information
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class AdditionDetail(APIView):

    def get_object(self, pk):
        try:
            return Addition.objects.get(id=pk)
        except Addition.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        ''' View a addition with the given pk or all addition on is_available true if pk is None'''

        if  pk is None:
            snippet = Addition.objects.filter(is_available=True)
            serializer = AdditionSerializer(snippet, many=True)

        else:
            snippet = self.get_object(pk)
            serializer = AdditionSerializer(snippet)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
            ''' Create a new addition on given number1 and number2'''  

            serializer = AdditionSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)                