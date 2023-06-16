from django.db import models
import importlib
from django.core import validators

# # Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  login_id = models.CharField(max_length=255, null=False)
  password = models.CharField(max_length=255, null=False)
  
class Champions(models.Model):
  champion = models.CharField(primary_key=True, max_length=255)
  line = models.CharField(max_length=512, null=True)
  position = models.CharField(max_length=100, null=True)
  CC = models.CharField(max_length=512, null=True) 
  
class Champion_rate(models.Model):
  champ_id = models.CharField(primary_key=True, max_length=255)
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  라인 = models.CharField(max_length=255, null=True),
  승률 = models.CharField(max_length=255, null=True),
  픽률 = models.CharField(max_length=255, null=True),
  밴률 = models.CharField(max_length=255, null=True),

class Champion_story(models.Model):
  champ_id = models.CharField(primary_key=True, max_length=255)
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  # champion = models.CharField(primary_key=True, max_length=255)
  url = models.CharField(max_length=255, null=True),
  text = models.CharField(max_length=255, null=True),
  story = models.CharField(max_length=255,null=True),
  
class Champion_tip(models.Model):
  champ_id = models.CharField(primary_key=True, max_length=255)
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  key = models.CharField(max_length=255, null=True),
  id = models.IntegerField(max_length=255, null=True),
  image_url = models.CharField(max_length=255,null=True),
  enemy_tips = models.CharField(max_length=255, null=True),
  ally_tips = models.CharField(max_length=255, null=True),
  
class Champion_counter(models.Model):
  champ_id = models.CharField(primary_key=True, max_length=255)
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  counter_name = models.CharField(primary_key=True, max_length=255, null=True),
  승률 = models. CharField(max_length=255, null=True),
  

class Champion_skill(models.Model):
  champ_id = models.CharField(primary_key=True, max_length=255)
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  passive = models.CharField(max_length=255, null=True),
  Q_name = models.IntegerField(max_length=255, null=True),
  W_name = models.CharField(max_length=255, null=True),
  E_name = models.CharField(max_length=255, null=True),
  R_name = models.CharField(max_length=255, null=True),  