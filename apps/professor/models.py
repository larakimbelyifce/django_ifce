from django.db import models

# Create your models here.
class professor(models.Model):
    nome= models.CharField(max_length=100,help_text="nome do professor")
    