import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import User


def generate_random_nickname():
    adjectives = ["즐거운", "행복한", "도전하는", "용감한", "친절한", "고독한", "고민하는", "멋진", "궁금한", "똑똑한", "졸린", "배고픈", "배부른", "귀여운"]
    nouns = ["나무늘보", "울버린", "거북이", "호랑이", "사자", "펭귄", "코끼리", "독수리", "토끼", "용", "너구리", "두더지", "하마", "북극곰", "빈투롱", "코알라", "캥거루"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return adjective + " " + noun

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))

    return otp

def send_otp_via_email(email, otp):
    subject = "[ORGO] 환영합니다! 이메일을 인증해 주세요."
    message = f"아래의 코드를 입력하면 회원가입이 완료됩니다.\nCODE: {otp}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])