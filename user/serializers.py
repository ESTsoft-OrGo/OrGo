from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    profileImage = serializers.ImageField(source='profile.profileImage', read_only=True)
    nickname = serializers.CharField(source='profile.nickname', read_only=True)
    about = serializers.CharField(source='profile.about', read_only=True)
    id = serializers.CharField(source='profile.user.id', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'profileImage', 'nickname', 'about', 'id','login_method']

    def validate(self, attrs):
        email_exists=User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("중복된 이메일입니다.")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user
    

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['user']