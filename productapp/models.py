from django.db import models

# Create your models here.
from userapp.models import User


class ProductCategory(models.Model):
    KIND = {
        ("food", "Food"),
        ("exercise", "Exercise")
    }
    description = models.CharField("설명", max_length=256)
    kind = models.CharField("종류", choices=KIND, null=False, max_length=20)

    def __str__(self):
        return self.kind


class ProductDetailCategory(models.Model):
    name = models.CharField("세부 종류", max_length=50)
    description = models.CharField("설명", max_length=256)
    category = models.ForeignKey(ProductCategory, related_name="category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, verbose_name="유저", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ProductDetailCategory, related_name="detail_category", on_delete=models.SET_NULL, null=True)

    name = models.CharField("이름", max_length=128)
    description = models.CharField("설명", max_length=256)
    difficulty = models.IntegerField("난이도")

    def __str__(self):
        return self.name


class Routine(models.Model):
    user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="제품", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField("수량", default=1)

    def __str__(self):
        return f"{self.product.name} by {self.user.fullname}"


class Challenge(models.Model):
    STATUS = (
        ("시작 전", "시작 전"),
        ("진행 중", "진행 중"),
        ("완료", "완료")
    )

    user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="루틴", on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=STATUS, max_length=20, default=STATUS[0][0])
    bind_number = models.IntegerField(null=True)

    def __str__(self):
        return self.status
