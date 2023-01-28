from django.db import models

# Create your models here.

__all__ = [
    "PlatformUser",
    "Book",
    "Topic",
]


class Book(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    # cover = models.ImageField() install Pillow first
    class Tag(models.IntegerChoices):
        LITERATURE = (0, "文学")
        POPULAR = (1, "流行")
        CULTURE = (2, "文化")
        LIFE = (3, "生活")
        ECOMAN = (4, "经管")
        TECH = (5, "科技")
        OTHER = (6, "其它")
    '''
    class SubTag(models.IntegerChoices):
        NOVEL = (0, "小说")
        LITERATURE = (1, "文学")
        FOREIGN = (2, "外国文学")
        CLASSICS = (3, "经典")
        CN = (4, "中国文学")
        ESSAY = (5, "随笔")
        JP = (6, "日本文学")
        MULAKAMI = (7, "村上春树")
        POEM = (8, "诗歌")
        FAIRYTALE = (9, "童话")
        FAMOUS = (10, "名著")
    '''
    book_tag = models.SmallIntegerField("标签", choices=Tag.choices, default=Tag.OTHER)
    
    def __str__(self) -> str:
        return self.bookname
    
#TODO: class Topic(models.Model)

        
        
