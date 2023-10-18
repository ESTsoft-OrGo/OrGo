from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.models import User
from .models import Study, Tag, GroupChat
from .serializers import StudySerializer, TagSerializer
from user.serializers import UserSerializer
from .pagination import PaginationHandlerMixin, StudyPagination
from django.utils import timezone
from rest_framework import status
import datetime


class StudyJoin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        study_id = request.data.get('study_id')
        study = get_object_or_404(Study, id=study_id)
        
        if study.participants.count() < study.max_participants:
            
            if request.user not in study.participants.all():
                
                if study.participants.count() == study.max_participants-1:
                    study.status = "진행중"
                    study.save()
                    
                study.participants.add(request.user)
                return Response({"message": "스터디 참가가 완료되었습니다."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "이미 참가한 스터디입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "참가 인원이 마감되었습니다."}, status=status.HTTP_400_BAD_REQUEST)


class StudyCancel(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        study_id = request.data.get('study_id')
        study = get_object_or_404(Study, id=study_id)
        
        if request.user in study.participants.all():
            
            if study.participants.count() == study.max_participants:
                study.status="모집중"
                study.save()
                
            groupChat = GroupChat.objects.get(study=study)
            if request.user in groupChat.participants.all():
                groupChat.participants.remove(request.user)
                
            study.participants.remove(request.user)
            return Response({"message": "스터디 참가가 취소되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "참가하지 않은 스터디입니다."}, status=status.HTTP_400_BAD_REQUEST)


class StudyList(APIView, PaginationHandlerMixin):
    pagination_class = StudyPagination
    serializer_class = StudySerializer
    
    def get(self, request, format=None, *args, **kwargs):
        studies = Study.objects.filter(is_active=True).order_by('-created_at')
        studies_count = Study.objects.filter(is_active=True).order_by('-created_at').count()
        
        page = self.paginate_queryset(studies)
        if page is not None:
            new_studies = []
            for study in page:
                
                current_time = timezone.localtime().strftime("%Y-%m-%d")
                save_time = study.end_date.strftime("%Y-%m-%d")
                current_date = datetime.datetime.strptime(current_time, "%Y-%m-%d")
                save_date = datetime.datetime.strptime(save_time, "%Y-%m-%d")
                
                if save_date < current_date:      
                    study.status = '종료'
                    study.save()
                
                study_serializer = StudySerializer(study).data
                leader = User.objects.get(id=study.leader.id)
                profile = UserSerializer(leader).data
                tags = Tag.objects.filter(study=study.id).values()
                study_info = {
                    "study": study_serializer,
                    "leader": profile,
                    "tags": tags
                }
                new_studies.append(study_info)
            
            data = {
                'studies': new_studies,
                'studies_all': studies_count
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'detail': '페이지가 존재하지 않습니다.'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class StudyCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        request_data = request.data.copy()
        request_data['leader'] = user.id
        request_data['is_active'] = True
        serializer = StudySerializer(data=request_data)
        # tag django에서 split으로 ,로 분할 해줌. 
        tags = request.data.get('tags').split(',')
        if serializer.is_valid():
            study = serializer.save()
            study.participants.add(user)
            for tag in tags:
                tag_data = {
                    'study': study.id,
                    'name' : tag
                }
                tag_serializer = TagSerializer(data=tag_data)
                if tag_serializer.is_valid():
                    tag_serializer.save()

            data = {
                "message" : "스터디 등록이 완료되었습니다."
            }
            return Response(data, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class StudyEdit(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        serializer = StudySerializer(study, data=request.data, partial=True)
        current_participants = list(study.participants.all())
        
        if int(request.data['max_participants']) < study.participants.count():
            data = {
                "message": "수정된 참가자 수가 현재 참가자 수보다 적습니다."
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            
            serializer.save()
            study.participants.set(current_participants)
            update_study = Study.objects.get(id=request.data['study_id'])
            
            if update_study.participants.count() == update_study.max_participants:
                update_study.status = "진행중"
                update_study.save()
            
            data = {
                "message" : "스터디 정보를 수정하였습니다."
            }
            return Response(data, status=status.HTTP_200_OK)
        
        errors = serializer.errors
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class StudyDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        study = Study.objects.get(id=request.data['study_id'])
        study.is_active = False
        study.save()
        
        data = {
            "message": "스터디를 삭제하셨습니다."
        }
        return Response(data, status=status.HTTP_200_OK)


class StudyView(APIView):
    def get(self, request):
        raw_study = Study.objects.get(id=request.data['study_id'])
        tags = Tag.objects.filter(study=raw_study).values()
        leader = UserSerializer(raw_study.leader)
        study = StudySerializer(raw_study)
        
        participants = UserSerializer(raw_study.participants.all(), many=True)
        
        data = {
            "study": study.data,
            "tags": tags,
            "leader": leader.data,
            "participants": participants.data
        }
        return Response(data, status=status.HTTP_200_OK)


class Tagadd(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        study_id = Study.objects.get(id=request.data['study_id'])
        
        if request.data['name']:
            tags = Tag.objects.create(study=study_id, name=request.data['name'])
            tag_serializer = TagSerializer(tags).data
            data = {
                "message": "태그 추가 완료",
                "tag": tag_serializer
            }
        else:
            data = {
                "message": "태그 추가 된게 없습니다.",
            }
        return Response(data, status=status.HTTP_201_CREATED)


class TagDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        tag = Tag.objects.get(id=request.data['tag_id'])
        tag.delete()
        
        data = {
            "message": "태그 삭제 성공"
        }
        return Response(data, status=status.HTTP_200_OK)