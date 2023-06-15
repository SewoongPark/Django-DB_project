from django.db import models
import importlib
from django.core import validators

# # Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  login_id = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  
class Champion(models.Model):
 
  champion = models.CharField(primary_key=True, max_length=255)
  line = models.CharField(max_length=512)
  position = models.CharField(max_length=100)
  CC = models.CharField(max_length=512) 
  #이미지 url로 가져올 경우를 대비해서 varchar로 설정
  # user = models.ForeignKey("User", on_delete=models.CASCADE)
  
# class Champion_rate(models.Model):
#   champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
#   라인 = models.CharField(max_length=255),
#   승률 = models.CharField(max_length=255),
#   픽률 = models.CharField(max_length=255),
#   밴률 = models.CharField(max_length=255),
  
# class Comment(models.Model):
#   comment_id = models.CharField(primary_key=True, max_length=100)
#   user_id = models.AutoField(models.ForeignKey("User", on_delete=models.CASCADE))  
#   champ = models.ForeignKey(Champion, on_delete=models.CASCADE)
#   user_comment = models.CharField(max_length=512)
#   total_comment = models.CharField(max_length=512)
#   best_comment = models.CharField(max_length=512)
#   rating = models.IntegerField(max_length=3)
  
# class WordCloud(models.Model):
#   cloud_id = models.AutoField(primary_key=True, max_length=100)
#   champ_id = models.ForeignKey("Champ", on_delete=models.CASCADE)
  