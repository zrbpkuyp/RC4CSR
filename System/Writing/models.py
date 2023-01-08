from django.db import models

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
    chap_num = models.IntegerField(max_length=1000)
    # tags = 
    # author = 
    # text = 
    def __str__(self) -> str:
        return self.topic
    