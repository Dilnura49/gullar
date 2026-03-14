from django.db import models

# Create your models here.
class katigoriya (models.Model):
 nomi=models.CharField(max_length=160)
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)

    

 class item (models.Model):
  nomi=models.CharField(max_length=150)
  narx=models.DecimalField(max_digits=15,decimal_place=3)
  katigoriya=models.ForeignKey(katigoriya,on_delete=models.CASCADE)
