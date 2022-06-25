from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not Specified')
    }

    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100)
    password = models.CharField("비밀 번호", max_length=256)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    gender = models.CharField("성별", max_length=80, choices=GENDER_CHOICES, null=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Coach(models.Model):
    KIND = {
        ("nutrition", "Nutrition"),
        ("fitness", "Fitness")
    }

    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    nickname = models.CharField("닉네임", max_length=50)
    phone_number = models.CharField("전화번호", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    kind = models.CharField("전문 분야", choices=KIND, null=False, max_length=20)