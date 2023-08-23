from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Study
from django.shortcuts import get_object_or_404

class StudyJoin(APIView):
    def post(self, request):
        study_id = request.data.get('study_id')
        study = get_object_or_404(Study, id=study_id)
        
        if study.participants.count() < study.max_participants:
            if request.user not in study.participants.all():
                study.participants.add(request.user)
                return Response({"message": "스터디 참가가 완료되었습니다."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "이미 참가한 스터디입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "참가 인원이 마감되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

class StudyCancel(APIView):
    def post(self, request):
        study_id = request.data.get('study_id')
        study = get_object_or_404(Study, id=study_id)
        
        if request.user in study.participants.all():
            study.participants.remove(request.user)
            return Response({"message": "스터디 참가가 취소되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "참가하지 않은 스터디입니다."}, status=status.HTTP_400_BAD_REQUEST)
