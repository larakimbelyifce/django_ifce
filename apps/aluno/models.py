from django.db import models

# Create your models here.
class aluno(models.Model):
    nome = models.CharField(max_length=100,help_text="nome do aluno")
    cpf = models.CharField(max_length=12,help_text="cpf do aluno")