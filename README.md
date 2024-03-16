## Seou's blog

### 2024-03-10 ~

# Install Django and Initial settings

> pip3 install django
> python3 -m venv .venv
> django-admin startproject config .

## Check Blog project structure

pyblog
|---config
| |-**init**.py
| |- asgi.py
| |- settings.py
| |- urls.py
| ㄴ wsgi.py
|-- manage.py
|-- templates/
|-- blog
ㄴㅡ users

## Implementing a post and comment modelseou

- comment 1:N link
  title| content
  post| text
  post2|text
  post3|text

- Post Table
  ID| title
  1| content
  2| content
  3| content

- 글과 연결된 댓글 테이블
  Id|Post Id| Comment
  1|1|comment 1번과 연결됨
  2|1|comment 1번과 연결됨
  3|3|comment 3번과 연결됨

1:N 관계로 테이블을 구성

## 모델 구현

> python3 manage.py startapp blog

config/settings.py

INSTALLED_APPS = [
"blog",
# 기존내용
. . .
]

#### blog/models.py 모델 추가

#### makemigration, migrate로 테이블 생성

> python3 manage.py makemigrations
> python3 manage.py migrate

## Post admin 구성

1. Superuser 생성

> python3 manage.py createsuperuser

2. 개발 서버실행, admin에 글 생성

> python3 manage.py runserver

![upload_img](img/1.png)
![upload_img](img/2.png)
![upload_img](img/3.png)
