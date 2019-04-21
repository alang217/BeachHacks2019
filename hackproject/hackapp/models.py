from django.db import models

# Create your models here.




class TextEntry(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=10000, blank=False)
    tone = models.CharField(max_length=255)
    emotion = models.CharField(max_length=255)
    professionalism = models.IntegerField()
    offensiveness = models.CharField(max_length=255)
    reading_level = models.IntegerField()


