from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegistroSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, validators=[validate_password])

  class Meta:
    model = User
    fields = ("username", "email", "password")

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data["username"],
      email=validated_data.get("email", ""),
      password=validated_data["password"],
    )
    return user
