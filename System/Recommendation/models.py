from django.db import models
from django.contrib.auth.models import User

# Create your models here.

__all__ = [
    "PlatformUser",
]

class PlatformUserManager(models.Manager):
    def get_by_user(self, user: User):
        result: PlatformUser = self.get(uid=user)
        return result

class PlatformUser(models.Model):
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    
    uid = models.OneToOneField(to=User, on_delete=models.CASCADE)

    nickname = models.CharField("昵称", null=True, unique=True, max_length=20)
    class Gender(models.IntegerChoices):
        MALE = (0, "男")
        FEMALE = (1, "女")

    gender = models.SmallIntegerField("性别", choices=Gender.choices)

    class Major(models.IntegerChoices):
        CHINESE = (0, "汉语言")
        FOREIGN = (1, "外国语")
        SOCIAL = (2, "社会学")
        POLITICAL = (3, "政治学")
        HISTORY = (4, "历史学")
        MATH = (5, "数学")
        PHYSICS = (6, "物理学")
        CHEMISTRY = (7, "化学")
        BIOLOGY = (8, "生物学")
        COMPUTER = (9, "计算机科学")
        PHILOSOPHY = (10, "哲学")
        PHYCHOLOGY = (11, "心理学")
        OTHERS = (12, "其他")

    major = models.SmallIntegerField("专业", choices=Major.choices, default=Major.OTHERS)

    class BOOK_TYPE(models.IntegerChoices):
        FICTION = (0, "小说、散文及其他文学作品")
        SOCIAL = (1, "社会学")
        POLITICAL = (2, "政治学")
        HISTORY = (3, "历史学")
        MATH = (4, "数学")
        PHYSICS = (5, "物理学")
        CHEMISTRY = (6, "化学")
        BIOLOGY = (7, "生物学")
        COMPUTER = (8, "计算机科学")
        PHILOSOPHY = (9, "哲学")
        PHYCHOLOGY = (10, "心理学")
        OTHERS = (11, "其他")

    type_preference = models.SmallIntegerField("书籍类型偏好", choices=BOOK_TYPE.choices)
    
    def __str__(self) -> str:
        return self.nickname

    def get_type(self=None) -> str:
        '''User一对一模型的必要方法'''
        return "PlatformUser"

    def get_user(self) -> User:
        '''User一对一模型的必要方法'''
        return self.uid

    def get_display_name(self) -> str:
        '''User一对一模型的必要方法'''
        return self.nickname

