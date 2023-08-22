from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Study, Tags
from .serializers import StudySerializer, TagSerializer
# Create your views here.

User = get_user_model()


## Study
class StudyList(APIView):
    def post(self, request):
        studies = Study.objects.all().values()
        new_studies = []
        for study in studies:
            writer = User.objects.get(id=study["leader_id"])
            profile = writer.profile
            
            pf_info = profile.__dict__
            pf_info['_state'] = ""
            
            post_info = {
                "post": study,
                "writer": pf_info
            }
            new_studies.append(post_info)
        
        data = {
            "studies": new_studies
        }
        return Response(data, status=status.HTTP_200_OK)


class StudyCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        request_data = request.data.copy()
        request_data['leader'] = user.id
        serializer = StudySerializer(data=request_data)
        
        # serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class StudyEdit(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        study.title = request.data['title']
        study.description = request.data['description']
        study.start_date = request.data['start_date']
        study.end_date = request.data['end_date']
        study.online_offline = request.data['online_offline']
        study.location = request.data['location']
        study.max_participants = request.data['max_participants']
        study.status = request.data['status']
        study.save()
        data = {
            "message":'study edit',
            "data": request.data,
        }
        return Response(data, status=status.HTTP_200_OK)


class StudyDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        study.is_active = False
        study.save()
        
        data = {
            "message": "delete complete"
        }
        return Response(data, status=status.HTTP_200_OK)