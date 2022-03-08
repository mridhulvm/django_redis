from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .serializers import AdditionSerializer
from .models import Addition


#for class based view
from rest_framework.views import APIView

#logging the information
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class AdditionAPIView(APIView):
    def get(self, request, format=None):
        ''' View a addition with the given id or all in id not given'''

        try:
            id = self.request.query_params.get('addition_id')
            # logger.error('post try:')
            logger.error(id)
        except:
            id = None


        if id is not None:
            try:
                calculation = Addition.objects.get(id = id, is_available = True)
                serializer = AdditionSerializer(calculation, many=False)
                # logger.error('addition serializer')
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        calculations = Addition.objects.filter(is_available = True)

        if calculations:
            serializer = AdditionSerializer(calculations,many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
                
    def post(self,request, format=None):
            ''' Create a new addition '''  

            serializer = AdditionSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)                