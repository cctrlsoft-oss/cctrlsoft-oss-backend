from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from core.serializers import RegistroSerializer


class PerfilView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response({
      "id": request.user.id,
      "username": request.user.username,
      "email": request.user.email,
    })


class RegistroView(APIView):
  def post(self, request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({"message": "Usuario creado", "user": user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
