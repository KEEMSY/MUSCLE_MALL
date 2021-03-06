from django.db import models

# Create your models here.
from userapp.models import User


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BoardCategory(models.Model):
    KIND = {
        ("notice", "notice"),
        ("free", "free"),
    }
    kind = models.CharField("종류", choices=KIND, null=False, max_length=20)
    description = models.CharField("설명", max_length=256)

    def __str__(self):
        return self.kind


class Board(BaseModel):
    user = models.ForeignKey(User, related_name="board_user", on_delete=models.CASCADE)
    category = models.ForeignKey(BoardCategory, related_name="category", on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250, error_messages={'error': '내용이 너무 깁니다.'})

    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name="comment_board", on_delete=models.CASCADE)

    content = models.CharField(max_length=128, error_messages={'error': '내용이 너무 깁니다.'})


class BoardLike(BaseModel):
    user = models.ForeignKey(User, related_name="like_user", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name="like_board", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "board"], name="unique_user_board_like")
        ]


class BoardBookmark(BaseModel):
    user = models.ForeignKey(User, related_name="bookmark_user", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name="bookmark_board", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "board"], name="unique_user_board_bookmark")
        ]
