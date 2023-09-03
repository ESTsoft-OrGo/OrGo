# OrGo

![index2](https://github.com/Hyunwooz/Django_Channels_Practice/assets/107661525/4718f314-a35d-463e-b28e-9705dafec488)

[오르고 바로가기](http://www.withorgo.site/)

```
해당 서비스를 이용해보실 수 있는 테스트 계정입니다.

 ID : test5@gmail.com
 PW : test2023
```

## 개요
```
안녕하세요. 🙇‍♂️

오르고는 오르미 교육생분들을 위한 커뮤니티이며 
오르미 1기, 2기 ... N기 모두가 이용할 수 있는 서비스 입니다.

백엔드 개발이라는 오름을 혼자가 아닌 "함께" 올라보세요!
그럼 우리 같이 ORGO!

1️⃣ 오르고는 자체 회원가입 뿐만 아니라 구글, 깃허브를 이용한 소셜 로그인을 지원하고 있습니다.
2️⃣ 오르고는 일상에서 찾아낸 소소한 행복을 공유할 수 있습니다.
3️⃣ 오르고는 혼자 공부 하는 것이 힘들 때 함께할 팀원들을 구할 수도 있습니다.
4️⃣ 오르고는 팔로워분들과 1:1 메시지를 통해 소통이 가능합니다.
```

##  팀원 소개

###  안녕하세요. Team OrGo 입니다!

|강현우|김이도|사수봉|이사랑|황봉수|
|:---:|:---:|:---:|:---:|:---:|
<img src="https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/722d5102-81f7-46a2-8afe-505595e57983" width="400" style="max-width: 100%;">|<img src="https://avatars.githubusercontent.com/u/96900790?v=4" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147091272142692352/KakaoTalk_Photo_2023-09-01-17-46-40.jpeg" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147088584428498964/IMG_0887.JPG" width="400" style="max-width: 100%;">|<img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147090595614031942/image.png" width="400" style="max-width: 100%;">|
|<a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a>|<a href="https://github.com/xkimido">🔗 xkimido</a>|<a href="https://github.com/su0797">🔗 su0797</a>|<a href="https://github.com/ra388">🔗 ra388</a>|<a href="https://github.com/bnbbbb">🔗 bnbbbb</a>|

저희는 백엔드 주니어 개발자 팀 OrGo입니다.

### 각자의 역할

![각자역할](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c6d855ac-13fe-431b-a9c8-5e131c218474)

## **[목차]**

1. [기능](#1-목표와-기능)
2. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)
3. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)
4. [전체 페이지](#4-전체-페이지)
5. [구현 기능 시연](#5-기능)
6. [개발하며 느낀점](#6-개발하며-느낀점)

## 1. 기능

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

-   https://api.withorgo.site/
-   Back-End Repo : https://github.com/ESTsoft-OrGo/OrGo

#### 2.3.2. Front-End

-   https://www.withorgo.site/
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
|채팅방 생성|chat/join/||
|채팅방 입장|ws:/chat/str:room_name/||
|메시지 보내기|ws:/chat/str:room_name/||
|Notify|||
|실시간 알림 받기|ws:/notify/str:user_id/||
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


### 메인 페이지
![www withorgo site_index html (1)](https://github.com/ESTsoft-OrGo/OrGo/assets/107661525/78033f41-a08d-4681-ba5b-dc09927a9b72)

### 세부 페이지
Figma : https://www.figma.com/file/8jeAIfOdZcYZ8ehctmA8yn/Untitled?type=design&node-id=2-54&mode=design&t=DPLaDoTa3ZSmgwT4-0
![스크린샷 2023-09-02 112048](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/2d97c668-c584-4225-b7fd-9b5f76ac746a)

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
### 6.1. 배운 점
#### 6.1.1 CGI와 WSGI, ASGI

CGI란?

Common Gateway Interface의 약자이며 웹 서버와 외부 프로그램을 연결해주는 표준화된 프로토콜입니다.

웹에 대한 수요가 증가함에 따라서 웹 서버에서 처리할 수 없는 정보가 요청되었을 경우,
그 처리를 외부 애플리케이션이 할 수 있도록 호출함으로써 중계 역할을 하고 있습니다.

CGI는 클라이언트의 요청이 발생할 때마다 프로세스를 추가로 생성하고 삭제하게 됩니다.
다수의 사용자가 동시에 요청할 경우 커널 리소스를 계속 생성/삭제하기 떄문에 오버헤드가 심해지고 성능 저하의 원인이 되기도 합니다.

WSGI란?

Web Server Gateway Interface의 약자이며 Python이 애플리케이션, 스크립트가 웹 서버와 통신하기 위한 인터페이스로 CGI를 모태로 만들어졌습니다.

WSGI의 경우 CGI와는 다르게 한 프로세스에서 모든 요청을 콜백(Callback)으로 받아 처리하게 됩니다.

간단히 설명하자면 웹 서버가 애플리케이션의 코드를 직접적으로 읽을 수 없으므로 중간의 미들웨어가 해당 코드를 읽어서 결과를 대신 반환해주는 역할을 한다고 보면 됩니다.

대표적인 WSGI Web Application에는 gunicorn 등이 있습니다.

WSGI의 경우에는 비동기적인 요청 처리에 단점이 있습니다. 하나의 동기적인 callable이 요청을 받아 응답을 리턴하는 방식이었는데, 이런 방식은 길게 유지되어야 하는 연결 - long-poll HTTP나 웹 소켓에는 적합하지 않습니다.

ASGI란?

Asynchronous Server Gateway Interface의 약자이며 Python에서는 asyncio, corutin과 같은 비동기 처리를 지원합니다. ASGI는 WSGI의 단점을 개선하기 위해 만들어졌습니다.
WSGI에 대한 호환성을 가지면서 비동기적인 요청을 처리할 수 있는 인터페이스입니다.

ASGI는 Websoket 프로토콜과 HTTP 2.0을 지원합니다.
대표적인 ASGI Web Application에는 Uvicorn 등이 있습니다.


#### 6.1.2 Django Channels
#### 6.1.3 우리가 배포에 Nginx와 Gunicorn,Uvicorn을 사용한 이유

Runserver를 이용해 서버 배포를 안하는 이유:

https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver # Django Docs

Django 공식 문서 참고

Runserver는 개발 단계에서 웹 애플리케이션을 빠르게 개발하고 테스트할 수 있도록 제공하는 기능이라고 말하며 프로덕션 환경에서는 Runserver를 사용하지 말라고 알려주고 있습니다. 
그 이유로는 보안 감사나 성능 테스트를 거치지 않았으며, 기능이 단순하고 대량 요청이나 동시 요청을 효율적으로 처리하지 못한다고 말하고 있습니다.

따라서 보안적, 성능적으로 효율적이지 못하기에 보통 Nginx와 Gunicorn을 같이 사용하여 배포하게 됩니다.

Nginx

동시 접속 처리에 특화된 웹서버로 클라이언트로 부터 HTTP 요청을 받아 해당하는 파일을
HTTP 통신을 통해 응답해주는 프로그램입니다.

웹서버 특성상 정적 컨텐츠 호스팅에 특화되어있으며, 이밖에 리버스 프록시, 캐싱, 로드 밸런싱 등 여러 역할을 수행하고 있습니다.

Nginx를 사용하지 않더라고 WAS가 직접 서비스를 제공해도 되지만 DB와 연결된 WAS의 보안을 강화할 수 있다는 장점이 존재합니다.

Gunicorn

Python WSGI로 웹서버(Nginx)로 부터 서버사이드 요청을 받으면 WSGI를 통해 서버 애플리케이션(Django)로 전달해주는 역할을 수행하고 있습니다.

WSGI의 경우 멀티쓰레드를 만들 수 있기 때문에, Request 요청이 많아지더라도 효율적으로 처리할 수 있습니다.

실제로 저희 프로젝트에 Gunicorn을 도입한 결과 응답 속도가 2~3초에서 1초 이내로 상당히 빨라지게 되었습니다.

Uvicorn

Uvicorn은 uvloop와 Httptools라는 것을 이용해서 ASGI를 구현한 서버입니다.
내장된 asyncio의 이벤트 루프 역할을 uvloop로 대체하여 동작함으로써 속도면에서 빠르라다고 합니다.

Uvicorn은 단일 프로세스로 동작하며, 일정 이상 트래픽이 넘어서면 한계점이 존재합니다.
이를 보안하기 위해 Gunicorn의 Worker들에 Uvicorn을 활용하여 배포하고 있습니다.
#### 6.1.3 실시간 메시징 기능 구현을 위한 HTTP 통신과 Socket 통신
**HTTP 프로토콜**

HTTP 프로토콜이란 인터넷 상에서 데이터를 주고받기 위한 서버/클라이언트 모델을 따르는 프로토콜을 이야기합니다.

HTTP 프로토콜 통신은 소켓 통신을 기반으로 하며 IP와 Port 번호 등이 존재하는 TCP/IP 헤더들이 붙여져 메시지가 송수신됩니다.

HTTP 프로토콜과 소켓 통신을 구분하는 이유는 HTTP 프로토콜의 경우 한쪽에서만 요청에 대한
응답을 하는 웹 통신에 특화되어있으며 이러한 통신 매커니즘은 소켓 통신과 다르기 때문입니다.

초기에 HTTP 프로토콜은 HTML 파일을 전송하는 의미를 가졌지만, 현재는 JSON과 Image 등 다양한 형식의 파일들을 전송할 수 있게 되었습니다.

데이터를 자주 주고받는 환경인 경우 소켓 통신이 유리하지만
그렇지 않는 환경이라면 HTTP 프로토콜 통신이 유리합니다.

HTTP에서 실시간 통신을 하는 방법에는 대표적으로 3가지가 있습니다.

- Polling
- Long Polling
- Streaming

**Polling**

브라우저가 일정한 주기마다 서버에 HTTP 요청을 보내는 방식입니다.

서버측 데이터 업데이트 유무를 클라이언트 쪽에선 예측할 수 없기에 이를 위해 일정한 주기를 반복하여 요청을 보내는 것입니다.

하지만 이러한 방식은 서버 및 네트워크 부하를 늘리는 악영향을 끼칠 수 있습니다.

**Long Polling**

Polling 방식의 단점인 서버 부하를 줄이며 실시간성을 높이기 위하 고안된 방식입니다.

HTTP 요청이 서버로 들어올 경우 요청에 대한 응답을 보낸 후 연결을 즉시 끊는 것이 아닌 일정시간을 대기합니다.

이 대기 시간안에서 데이터의 변경이 일어날 경우 바로 클라이언트 측으로 응답을 보내고 응답을 받은 클라이언트는 다시 서버에 요청을 보내는 방식입니다.

Long Polling 방식은 Polling 방식의 단점을 보안하기 위해 나왔지만 다량의 클라이언트와 연결된 경우, 데이터 변경이 자주 일어나는 경우 오히려 서버에 큰 부담을 줄 수도 있습니다.

**Streaming**

Streaming은 서버가 요청을 받았을 경우 해당 요청에 대한 응답을 완료하지 않은 상태에서 데이터를 계속 보내는 방식입니다. 따라서 클라이언트는 응답을 받았다 하더라도 연결을 끊고 다시 요청을 보내는 과정없이 계속하여 응답을 받아 처리할 수 있습니다.

이 방식의 큰 단점은 클라이언트에서 서버쪽으로 데이터를 보내는 것이 힘들다는 점이 있습니다. 양방향 통신이 아닌 단방향 통신에 가깝습니다.

**Websocket**

HTTP 프로토콜의 경우 실시간성이 떨어지는 단점이 있어 이를 보안하기 위해 Websocket이라는 기술이 도입되었습니다.

Websocket은 HTTP 프로토콜과 다르게 상태(Stateful) 프로토콜이며, 연결을 유지한채 실시간 양뱡향 통신 혹은 데이터 전송이 가능한 프로토콜을 말합니다.

클라이언트와 서버가 한번 연결되면 같은 연결을 이용해 통신하므로 TCP 커넥션 비용을 아낄 수 있습니다.

Websocket은 현재 채팅,온라인 게임, 화상 회의 등 많은 분야에서 사용되고 있습니다

### 6.2. 느낀 점
#### 강현우
#### 김이도
#### 사수봉
#### 이사랑
#### 황봉수
## 마치며



