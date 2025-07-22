import time
import re
import cloudinary
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import authenticate
from .serializers import RoleSerializer, UserSerializer, CustomTokenObtainPairSerializer,LogoutSerializer
from .models import Role, User
from User.serializers import (CustomTokenObtainPairSerializer, UserSerializer)
from User.models import User
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from datetime import timedelta
from django.conf import settings


# --- Registro de usuario ---
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # --- Enviar correo de bienvenida ---
            subject = '¡Bienvenido a !'
            from_email = settings.EMAIL_HOST_USER
            to = [user.email]
            html_content = render_to_string('welcome_email.html', {
                'user_first_name': user.first_name,
                'year': timezone.now().year,
               # 'logo_url': 'https://raw.githubusercontent.com/Web-Developers2-0/2025-Practica_Profesionalizante/main/frontend/src/assets/images/logo_blanco.png',
            })
            try:
                msg = EmailMultiAlternatives(subject, '', from_email, to)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print(f"Correo de bienvenida enviado a {user.email}")
            except Exception as e:
                print(f"Error al enviar el correo de bienvenida: {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(email=email, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data['access'],
                    'refresh-token': login_serializer.validated_data['refresh'],
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    
class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]
