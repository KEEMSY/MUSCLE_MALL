from django.db import models

# Create your models here.
from userapp.models import User


class ProductCategory(models.Model):
    KIND = {
        ("food", "Food"),
        ("exercise", "Exercise")
    }
    name = models.CharField("이름", max_length=30)
    description = models.CharField("설명", max_length=256)
    kind = models.CharField("종류", choices=KIND, null=False, max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(" 이름", max_length=128)
    description = models.CharField("설명", max_length=256)
    difficulty = models.IntegerField("난이도")
    category = models.OneToOneField(ProductCategory, verbose_name="종류", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Routine(models.Model):
    user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE)
    name = models.CharField("루틴 이름", max_length=50)
    description = models.CharField("설명", max_length=256)
    product = models.ForeignKey(Product, verbose_name="제품", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, verbose_name="루틴", on_delete=models.CASCADE)
    quantity = models.IntegerField()



