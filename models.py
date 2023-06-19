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
 
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  line = models.CharField(max_length=255, null=True)
  winrate = models.CharField(max_length=255, null=True)
  pickrate = models.CharField(max_length=255, null=True)
  banrate = models.CharField(max_length=255, null=True)

class Champion_story(models.Model):
  
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  url = models.CharField(max_length=255, null=True),
  text = models.CharField(max_length=255, null=True)
  story = models.CharField(max_length=255,null=True)
  
class Champion_tip(models.Model):
  
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  key = models.CharField(max_length=255, null=True)
  id = models.IntegerField(null=True)
  imageurl = models.CharField(max_length=255,null=True)
  enemytips = models.CharField(max_length=255, null=True)
  allytips = models.CharField(max_length=255, null=True)
  
class Champion_counter(models.Model):
  
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  countername = models.CharField(max_length=255, null=False)
  winrate = models. CharField(max_length=255, null=True)
  

class ChampionSkill(models.Model):
 
  champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
  passive = models.CharField(max_length=255, null=True)
  Q_name = models.CharField(max_length=255, null=True)
  W_name = models.CharField(max_length=255, null=True)
  E_name = models.CharField(max_length=255, null=True)
  R_name = models.CharField(max_length=255, null=True)