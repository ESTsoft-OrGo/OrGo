from django.urls import path
from .views import StudySearch, StudyJoin, StudyCancel

app_name = 'study'

urlpatterns = [
    path("search/", StudySearch.as_view(), name='search'),
    # 참가
    path("join/", StudyJoin.as_view(), name='join'),
    path('join/cancel/', StudyCancel.as_view(), name='cancel')
]