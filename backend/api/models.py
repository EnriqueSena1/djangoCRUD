from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_aluno = models.BooleanField(default=False)



# # Create your models here.
# class Funcionario(models.Model):
#     nome = models.CharField( max_length=255, null=False, blank=False)
#     sobrenome = models.CharField(max_length=255, null=False, blank=False)
#     cpf = models.CharField(max_length=14, null=False, blank=False)
#     tempoDeServico = models.IntegerField(default=0, null=False, blank=False)
#     remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

#     def __str__(self):
#         return f"{self.nome} {self.sobrenome}"
    
# #--------------------------------------------------------------------------------------------------------------------------#   

# class Categoria(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)

#     def __str__(self):
#         return f"{self.nome}"
    
# #--------------------------------------------------------------------------------------------------------------------------#   

# class Produto(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     descricao = models.TextField(null=True, blank=True)
#     valor = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
#     quantidade = models.IntegerField(default=0, null=False, blank=False)
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nome}"