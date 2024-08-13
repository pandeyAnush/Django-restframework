from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Cars
from .serializers import *

class CarList(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]
    def get(self,request):

        objs = Cars.objects.all()
        if objs:
            return Response({
                "error": False,
                "data": CarListSerializer(objs, many=True, context={'request': request}).data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": False,
                "data": "Car list not found.",
                "status": status.HTTP_204_NO_CONTENT
            }, status=status.HTTP_204_NO_CONTENT)


class SecondCarList(APIView):
    
    def get(self,request):
        user = request.user
        
        if user.is_authenticated:

            objs = Cars.objects.all()
            if objs:
                return Response({
                    "error": False,
                    "data": CarListSerializer(objs, many=True, context={'request': request}).data,
                    "status": status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": False,
                    "data": "Car list not found.",
                    "status": status.HTTP_204_NO_CONTENT
                }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                "error": False,
                "data": "Unauthorized User.",
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        
class CarAPI(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "error": False,
            "data": "Car has been register.",
            "status": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)
        return Response({
            "error": True,
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
