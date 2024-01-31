from django.conf import settings
from django.db import models
from random import choices
from string import ascii_letters, digits


def gen_code():
    """
    生成一个长度为10的随机代码，并检查它是否尚未在Room模型中使用。
    如果已经被使用，继续生成新代码直到找到唯一的代码。返回该唯一代码。
    """
    length = 10
    while True:
        code = "".join(choices(ascii_letters + digits, k=length))
        if Room.objects.filter(r_code=code).count() == 0:
            return code

# Create your models here.


class Room(models.Model):
    r_code = models.CharField(max_length=12, unique=True, default="")
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.r_code


class Course(models.Model):
    name = models.CharField(max_length=20, unique=True,
                            help_text="课程名", verbose_name="课程名")
    info = models.TextField(help_text="课程信息", verbose_name="信息", blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="课程价格", verbose_name="价格")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text="课程讲师", verbose_name="讲师")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
