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
