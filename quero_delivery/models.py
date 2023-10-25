from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    num_casa = models.BigIntegerField(default=0)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    referencia = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.id

class Pedido(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    produtos = models.JSONField()
    def __str__(self):
        return self.produtos
    