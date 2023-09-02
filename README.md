# OrGo
# 이스트소프트 오르미 수강생 커뮤니티 오르고

##  팀원 소개

###  안녕하세요. Team OrGo 입니다!

|강현우|김이도|사수봉|이사랑|황봉수|
|:---:|:---:|:---:|:---:|:---:|
<img src="https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/722d5102-81f7-46a2-8afe-505595e57983" width="400" style="max-width: 100%;">|<img src="https://avatars.githubusercontent.com/u/96900790?v=4" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147091272142692352/KakaoTalk_Photo_2023-09-01-17-46-40.jpeg" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147088584428498964/IMG_0887.JPG" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147090595614031942/image.png" width="400" style="max-width: 100%;">|
|<a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a>|<a href="https://github.com/xkimido">🔗 xkimido</a>|<a href="https://github.com/su0797">🔗 su0797</a>|<a href="https://github.com/ra388">🔗 ra388</a>|<a href="https://github.com/bnbbbb">🔗 bnbbbb</a>|

저희는 백엔드 주니어 개발자 팀 OrGo입니다.

**[목차]**

1. [기능](#1-목표와-기능)
2. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)
3. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)
4. [전체 페이지](#4-전체-페이지)
5. [기능](#5-기능)
6. [개발하며 느낀점](#6-개발하며-느낀점)

## 1. 기능

### 1.1. 목표

- 오르미 교육생들을 위한 커뮤니티
- 오르미 1기 2기 … N기가 모두가 이용할 수 있는 사이트

### 1.1. 주요 기능

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

### 2.1. 개발 환경

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

### 2.2. 배포 환경

#### 2.2.1. Back-End

-   Aws Lightsail
-   Nginx
    -   wsgi : gunicorn
-   asgi : uvicorn
-   Redis Stack == 6.2.6
-   PostgreSQL == 15.4
-   AWS S3

#### 2.2.2. Front-End

-   GitHub Pages

### 2.3. 배포 URL

#### 2.3.1. Back-End

-   http://43.200.64.24/
-   Back-End Repo : https://github.com/ESTsoft-OrGo/OrGo

#### 2.3.2. Front-End

-   http://www.withorgo.site/
-   Front-End Repo : https://github.com/ESTsoft-OrGo/Orgo-FE

## 3. 프로젝트 구조와 개발 일정

### 3.1. Entity Relationship Diagram
 ![Untitled](https://github.com/ESTsoft-OrGo/OrGo/assets/95666574/610374a4-d7d9-4b2d-b95a-2750f0b1f3ba)

### 3.2. API 명세서

#### 3.2.1. API 명세서: https://withorgo.notion.site/API-15bb92089e5048df8bf9a1916bba61d3?pvs=4

### 3.3. URL 설계
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

### 3.4. 프로젝트 설계 및 프로세스

#### 3.4.1. Architecture

![5](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/90eed4d4-f327-4fac-a26e-5f2847c1d195)

#### 3.4.2. Wsgi와 Asgi

![1](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/635c5a7d-c7ec-42ee-9dee-4c3a30067fee)

#### 3.4.3. Django Channels와 Redis

![2](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/8c8d2a5d-fcfb-4b43-bd78-65a1ae6f7bb4)

#### 3.4.4. Django의 시그널과 Redis

![3](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/295fdb44-48e1-40d6-ac77-35121c6aacc2)
![4](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/6caf6093-7556-450c-8403-f34a414702fe)

#### 3.4.5. 폴더 트리
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
### 3.5. 개발 일정

#### 3.5.1. 개발 일정

-   2023.08.17 ~ 2023.09.01
-   프로젝트 개발 일정: https://withorgo.notion.site/d52779f12ac547dabc1240320ef4aeb2?v=fb0701095b3840218a980c13305cda34&pvs=4

![스크린샷 2023-09-01 141622](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/f9bae29d-0fbe-4e28-b771-2ef2dfe5c803)

#### 3.5.2. 기술 스택

-   Python
-   Django
-   PostgreSQL
-   HTML
-   바닐라 JS
-   CSS

## 4. 전체 페이지

Figma : https://www.figma.com/file/8jeAIfOdZcYZ8ehctmA8yn/Untitled?type=design&node-id=2-54&mode=design&t=DPLaDoTa3ZSmgwT4-0

![스크린샷 2023-09-01 171533](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/2845b2b3-79fd-426b-8ced-fb044e43562c)

## 5. 기능

### 5.1. 유저 기능

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

-   프로필 변경
    ![profile-update](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c44d5786-15da-4ae0-b855-335086027031)

-   마이 페이지
    ![profile](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/04f44027-4108-4134-9e7c-7243dcd31e4b)

### 5.2. 알림

-   알림 기능
    ![notification](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/6ca495b2-3e21-49d0-be5d-922a01cb048c)

### 5.3. 1:1 채팅

-   채팅방 생성
    ![채팅방생성](https://github.com/Hyunwooz/Django_Channels_Practice/assets/107661525/971d0b5f-6426-4c9e-a8f8-9d2a66253149)

-   채팅방 삭제
    ![채팅방삭제](https://github.com/Hyunwooz/Django_Channels_Practice/assets/107661525/d5770cf9-fef8-4d9d-8c9e-170384568905)

-   1:1 채팅 기능
    ![direct-message](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/7fe5321c-203a-4e2f-b569-e074079df4fc)

### 5.4. 게시물 기능

-   생성
    ![post_write](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/a8ad9084-fce3-4a9c-b5f3-8c606da97fca)

-   목록
    ![post_read](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c7be8804-b155-433b-9168-8c3601045e9e)
    
-   수정
    ![post_edit](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/30954fc4-7526-427f-a3b9-60208a30bcb3)

-   삭제
    ![post_delete](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c0c109f9-340a-489b-8fb0-67da1e49258c)

### 5.5. 댓글 기능

-   생성
    ![comment_write](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/12f4e12e-a507-4797-ad77-fcd20d6c6ef8)

-   답글
    ![re_comment](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/58efa59b-7bd1-4aec-b9ea-85d6e0912ad7)

-   삭제
    ![comment_delete](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/468145af-8e88-4626-81cc-afcee2ec3b07)

### 5.6. 좋아요 기능

-   좋아요 / 취소
    ![좋아요](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/ab8daad8-7435-49d2-b4b0-b36ab8221b3f)

### 5.7. 팔로우 기능

-   팔로우 / 언팔로우
    ![follow_full](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/f724a0f8-f057-41a5-897d-d9549fac4e54)

### 5.8. 스터디 기능

-   생성
    ![study-create](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/82acb040-d386-463d-bea2-f0263d2e78ff)

-   삭제
    ![study-delete](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/be612a12-d946-48b5-a78a-621567a2a368)

-   수정
    ![study-update](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/28191658-3059-40f4-b39f-f8c92509cee8)

-   목록 / 페이지네이션
    ![study-list](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/935eb569-0983-4148-b2e4-b0d87cb5ae33)
    
-   참가 / 참가 취소
    ![study-join-quit](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c814963f-c08b-4b0c-8cb8-ec93d7c0c48d)

### 5.9. 검색 기능

-   검색 기능
    ![search](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/8c1e9acf-4995-4908-b1c0-bc348bdae81e)

## 6. 개발하며 느낀점

### 마치며



