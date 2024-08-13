from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


def get_token(user):
    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginAPI(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except Exception as e:
            return Response({'error': True, 'data': str(e)},status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password, request=request)
        if user is None:
            response = {
                'error':True,
                "status_code": status.HTTP_401_UNAUTHORIZED,
                'data': "Invalid email or password.",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        else:
            if user.is_active:
                jwt_access_token = get_token(user)
                response = {
                    'status_code': status.HTTP_200_OK,
                    'data': 'Logged in successfully.',
                    'access_token': jwt_access_token["access"],
                    'refresh_token': jwt_access_token["refresh"],
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'error':True,
                    'status_code': status.HTTP_401_UNAUTHORIZED,
                    'data': 'Please contact to authorized person to verify your account.',
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)