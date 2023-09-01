# OrGo
# 이스트소프트 오르미 수강생 커뮤니티 오르고

##  팀원 소개

###  안녕하세요. Team OrGo 입니다!

|강현우|김이도|사수봉|이사랑|황봉수|
|:---:|:---:|:---:|:---:|:---:|
<img src="" width="400">|<img src="" width="400">|<img src="" width="430">|<img src="" width="400">|<img src="" width="400">|
|<a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a>|<a href="https://github.com/xkimido">🔗 xkimido</a>|<a href="https://github.com/su0797">🔗 su0797</a>|<a href="https://github.com/ra388">🔗 ra388</a>|<a href="https://github.com/bnbbbb">🔗 bnbbbb</a>|

저희는 백엔드 주니어 개발자 팀 OrGo입니다.

**[목차]**

1. [목표와 기능](#1-목표와-기능)
2. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)
3. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)
4. [전체 페이지](#4-전체-페이지)
5. [기능](#5-기능)
6. [개발하며 느낀점](#6-개발하며-느낀점)

## 1. 목표와 기능

### 1.1 목표

- 오르미 교육생들을 위한 커뮤니티
- 오르미 1기 2기 … N기가 모두가 이용할 수 있는 사이트

### 1.2 주요 기능

-   회원가입 및 로그인 
-   소셜 로그인 (GitHub, Google)
-   JSON Web Token 인증 방식
-   프로필 CRU
-   1대1 채팅 
-   게시글, 사용자, 스터디 검색 기능
-   댓글 CRD
-   Follow / Unfollow 기능
-   좋아요
-   스터디 모임 CRUD
-   스터디 리스트 페이지네이션
-   댓글, 좋아요, 팔로우 실시간 알림 기능

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

-   Python == 3.11.3
-   Django == 4.2.4
-   channels == 4.0.0
-   channels-reids == 4.0.0
-   psycopg2 == 2.9.7
-   Pillow == 10.0.0
-   boto3 == 1.28.38
-   django-storages == 1.13.2
-   daphne == 4.0.0
-   Twisted == 22.10.0
-   django-cors-headers == 4.2.0
-   djangorestframework == 3.14.0

### 2.2 배포 환경

#### Back-End

-   Aws Lightsail
-   Nginx
    -   wsgi : gunicorn
-   asgi : uvicorn
-   Redis Stack == 6.2.6
-   PostgreSQL == 15.4
-   AWS S3

#### Front-End

-   GitHub Pages

### 2.2 배포 URL

#### Back-End

-   http://43.200.64.24/
-   Back-End Repo : https://github.com/ESTsoft-OrGo/OrGo

#### Front-End

-   http://www.withorgo.site/
-   Front-End Repo : https://github.com/ESTsoft-OrGo/Orgo-FE

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
 ![Untitled](https://github.com/ESTsoft-OrGo/OrGo/assets/95666574/610374a4-d7d9-4b2d-b95a-2750f0b1f3ba)

### 3.2 API 명세서

#### API 명세서: https://withorgo.notion.site/API-15bb92089e5048df8bf9a1916bba61d3?pvs=4

### 3.3 URL 설계
|이름|URL|비고|
|------|---|---|
|User|||
|로그인|user/login/||
|회원가입|user/join/||
|소셜 로그인|user/login/provider||
|프로필|user/profile/||
|프로필 수정|user/profile/update/||
|비밀번호 변경|user/profile/change-password/||
|회원탈퇴|user/profile/delete/||
|Post|||
|목록|post/||
|글쓰기|post/write/||
|수정|post/edit/||
|삭제|post/delete/||
|뷰|post/view/||
|Search|||
|검색|post/search/||
|Like|||
|좋아요|post/like/||
|좋아요 취소|post/unlike/||
|Follow|||
|팔로잉|user/follow/|Follow와 Unfollow 기능 둘다 함.|
|Comment|||
|쓰기|post/comment/write/||
|삭제|post/comment/delete/||
|대댓글 쓰기|post/re-comment/write/||
|Study|||
|목록|study/?page=number||
|생성|study/create/||
|참가|study/join/||
|참가 취소|study/join/cancle/||
|수정|study/edit/||
|삭제|study/delete/||
|tag 생성|study/tag/write/||
|tag 삭제|study/tag/delete/||
|Chat|||
|참여한 목록|chat/list/||
|생성 가능한 채팅방 목록|chat/following/|팔로잉한 유저만 채팅방 생성 가능|
|참가할 채팅방|chat/join/||
|Notify|||
|알림 목록|notify/||

### 3.4 프로젝트 구조
```
📦OrGo
 ┣ 📂Orgo
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜wsgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┣ 📂chat
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜consumers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routing.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂notify
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜consumers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routing.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂post
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂study
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜pagination.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂user
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tokens.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
### 3.5 개발 일정

#### 개발 일정

-   2023.08.17 ~ 2023.09.01
-   프로젝트 개발 일정: https://withorgo.notion.site/d52779f12ac547dabc1240320ef4aeb2?v=fb0701095b3840218a980c13305cda34&pvs=4

![스크린샷 2023-09-01 141622](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/f9bae29d-0fbe-4e28-b771-2ef2dfe5c803)

#### 기술 스택

-   Python
-   Django
-   PostgreSQL
-   HTML
-   바닐라 JS
-   CSS

## 4. 전체 페이지

## 5. 기능
### 유저 기능
-   전체 기능
    ![full-process](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/ae976b2a-f2f2-4593-b826-db16dab1eddf)
-   회원가입
    ![join](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/776231be-2552-4e76-89aa-6fe7069e81b0)
-   로그인
    ![login](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/d34781b2-c27d-4d4b-97c1-f87d6587683a)
-   비밀번호 변경
    ![change-password](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/2b7631a4-e513-40d4-b122-e2ed679b8b45)
-   회원 탈퇴
    ![delete](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/885a5651-c64d-4cc5-a282-3b975a6eb467)
-   로그아웃
    ![logout](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/9c7d293f-3484-413a-b0b0-9f1612ab06f9)
-   소셜 로그인
    ![social-login](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/7f951421-dabc-44dc-a5d8-6ca8426b81db)






## 6. 개발하며 느낀점

### 마치며



