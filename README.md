# OrGo
# 이스트소프트 오르미 수강생 커뮤니티 오르고

##  팀원 소개

**[목차]**

1. [목표와 기능](#1-목표와-기능)
2. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)
3. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)
4. [전체 페이지](#4-전체-페이지)
5. [기능](#5-기능)
6. [추가 기능](#6-추가-기능)
7. [개발하며 느낀점](#7-개발하며-느낀점)

## 1. 목표와 기능

### 1.1 목표
- 오르미 교육생을 위한 커뮤니티
- 실제로 서비스가 가능한 주제로 선정
- 오르미 1기 2기 … N기가 모두가 이용할 수 있는 사이트

### 1.2 주요 기능
-   회원가입 및 로그인 
-   Github 로그인
-   JSON Web Token 인증 방식
-   Profile CRU
-   유저 사이 Follow / Unfollow 기능
-   1대1 채팅 
-   제목 검색
-   게시글 검색
-   스터디 검색
-   댓글 CRD
-   맘에드는 게시글 좋아요

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

- Python == 3.11.3
- Django == 4.2.4
- Pillow==10.0.0


### 2.2 배포 환경

#### Back-End
-   Aws Lightsail
-   Nginx
-   uwsgi

#### Front-End
-   

### 2.2 배포 URL

#### Back-End
-   
-   Back-End Repo : https://github.com/ESTsoft-OrGo/OrGo
#### Front-End
-   
-   Front-End Repo : https://github.com/ESTsoft-OrGo/Orgo-FE

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
 ![Untitled](https://github.com/ESTsoft-OrGo/OrGo/assets/95666574/610374a4-d7d9-4b2d-b95a-2750f0b1f3ba)

### 3.2 URL 설계
|이름|URL|비고|
|------|---|---|
|User|||
|로그인|user/join/||
|회원가입|user/login/||
|소셜 로그인|user/login/<provider>||
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
|좋아요|Chatbot/lounge/||
|좋아요 취소|Chatbot/detail/||
|Follow|||
|팔로잉|user/follow/|Follow와 Unfollow 기능 둘다 함.|
|Comment|||
|쓰기|post/comment/write/||
|삭제|post/comment/delete/||
|수정|post/comment/edit/||
|대댓글 쓰기|post/re-comment/write/||
|Study|||
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

### 3.3 프로젝트 구조

### 3.4 개발 일정

#### 개발 일정

- 2023.08.17 ~ 2023.09.01

#### 기술 스택

-   Python
-   Django
-   PostgreSQL
-   HTML
-   바닐라 JS
-   CSS

## 4. 전체 페이지

## 5. 기능

## 6. 추가 기능

## 7. 개발하며 느낀점

### 마치며



