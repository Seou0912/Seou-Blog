from django.shortcuts import render, redirect
from blog.models import Post, Comment  # Post 모델을 사용하기 위해 import


# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # 모든 객체를 가진 QuerySet
    # 템플릿에 전달할 dict
    context = {
        "posts": posts,
    }
    # 3번째 인수로 템플릿에 데이터 전달
    return render(request, "post_list.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)  # 현재 포스트에 대한 댓글만 조회

    if request.method == "POST":
        # textarea의 "name" 속성값("comment")를 가져온다.
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )

    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "post_detail.html", context)


def post_add(request):
    # POST is already
    if request.method == "POST":
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]  # image file
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,  # Pass the image file when creating an object
        )
        return redirect(f"/posts/{post.id}/")
    # GET is already
    else:
        print("method GET")
        # print(request.POST)  # POST 메서드로 전달된 데이터를 출력한다.
    # POST and GET are already
    return render(request, "post_add.html")
