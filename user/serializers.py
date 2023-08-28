from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    profileImage = serializers.ImageField(source='profile.profileImage', read_only=True)
    nickname = serializers.CharField(source='profile.nickname', read_only=True)
    about = serializers.CharField(source='profile.about', read_only=True)
    id = serializers.CharField(source='profile.user.id', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'profileImage', 'nickname', 'about', 'id']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if User.objects.filter(email=email).exists():
            raise ValidationError("중복된 이메일입니다.")

        if password != password_confirm:
            raise ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")

        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password_confirm")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user
    

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['user']