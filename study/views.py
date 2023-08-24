from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404
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
    # permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        request_data = request.data.copy()
        request_data['leader'] = user.id
        serializer = StudySerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "study create complete"
            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class StudyEdit(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        serializer = StudySerializer(study, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "study edit complete"
            }
            return Response(data, status=status.HTTP_200_OK)
        
        errors = serializer.errors
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class StudyDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        study.is_active = False
        study.save()
        
        data = {
            "message": "study delete complete"
        }
        return Response(data, status=status.HTTP_200_OK)


class StudyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        rew_study = Study.objects.get(id=request.data['study_id'])
        tags = Tags.objects.filter(Study=rew_study).values()
        
        study = rew_study.__dict__
        study['_state'] = ""
        
        data = {
            "study":study,
            "tags":tags
        }
        return Response(data, status=status.HTTP_200_OK)


class TagWrite(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        user = User.objects.get(email=user)
        study_id = request.data.get('Study')
        serializer = TagSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                study = get_object_or_404(Study, id=study_id, leader=user.id)
            except Http404:
                data={
                    "error": "leader가 아닙니다."
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            data = {
                "message": "tag write complete"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class TagEdit(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tag = Tags.objects.get(id=request.data['tag_id'])
        tag.name = request.data['name']
        tag.save()
        
        data = {
            "message": "tag edit complete"
        }
        
        return Response(data, status=status.HTTP_200_OK)


class TagDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        tag = Tags.objects.get(id=request.data['tag_id'])
        tag.delete()
        
        data = {
            "message": "tag delete complete"
        }
        return Response(data, status=status.HTTP_200_OK)