import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import User


def generate_random_nickname():
    adjectives = ["즐거운", "행복한", "도전하는", "용감한", "친절한", "고독한", "고민하는", "멋진", "호기심 많은", "똑똑한"]
    random_adjective = random.choice(adjectives)

    return random_adjective + " 오르미"

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))

    return otp

def send_otp_via_email(email, otp):
    subject = "[ORGO] 환영합니다! 이메일을 인증해 주세요."
    message = f"아래의 코드를 입력하면 회원가입이 완료됩니다.\nCODE: {otp}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])