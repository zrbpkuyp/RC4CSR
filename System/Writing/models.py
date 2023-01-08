from django.db import models
# from System.models import PlatformUser

# Create your models here.

__all__ = [
    'Pencraft',
]

class Pencraft(models.Model):
    """Pencraft

    :param models: To be completed
    :type models: To be completed
    """
    topic = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    chap_num = models.IntegerField(default=0)
    # tags = 
    # author : PlatformUser = models.ForeignKey(PlatformUser,on_delete=models.CASCADE)
    # text = 
    def __str__(self) -> str:
        return self.topic
    