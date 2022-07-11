from django.db import models


# Create your models here.
from userapp.models import User


class BoardCategory(models.Model):
    KIND = {
        ("Notice", "Notice"),
        ("free", "Free"),
    }
    kind = models.CharField("종류", choices=KIND, null=False, max_length=20)
    description = models.CharField("설명", max_length=256)

    def __str__(self):
        return self.kind


class Board(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    category = models.ForeignKey(BoardCategory, related_name="category", on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250, error_messages={'error': '내용이 너무 깁니다.'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
