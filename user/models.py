from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('이미 있는 Email 입니다.')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            created_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # create_user
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    # create_superuser
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    login_method = models.CharField(default='email',max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    nickname = models.CharField(default='닉네임', max_length=50, null=True, blank=True)
    profileImgae = models.ImageField(upload_to='user/media',null=True,blank=True)
    about = models.TextField(default='자신을 소개해주세요 :)',null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follower(models.Model):
    target_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target_id')
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_id')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)