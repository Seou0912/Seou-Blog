from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField("title", max_length=100)
    content = models.TextField("content")
    thumbnail = models.ImageField("thumbnail img", upload_to="post", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("comment")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"
