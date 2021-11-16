from django.db import models
from django.conf import settings



class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Post(TimestampedModel):    

    STATE_CHOICES = (        
            ('진행', 'doing'),
            ('예정', 'plan'),
            ('종료','end'),            
        )
    # photo = models.ImageField(upload_to="challenges/post/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    title = models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)
    host = models.CharField(max_length=16)
    award = models.CharField(max_length=6)
    period1 = models.DateField(max_length=14)
    period2 = models.DateField(max_length=14)    
    Participant = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField('Tag', blank=True)
    state = models.CharField(max_length=5, null=False, choices=STATE_CHOICES)
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name