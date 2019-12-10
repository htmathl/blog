from django.db import models

class Postagem(models.Model):
    opcao_tema = [
        ('ROM', 'Romance'),
        ('GAM', 'Games'),
        ('Pro', 'Professão')
    ]

    nome  = models.CharField(max_length=50)
    idade = models.IntegerField(default=1)
    email = models.CharField(max_length=50)
    texto_blog = models.CharField(max_length=150)
    tema = models.CharField(max_length=3, choices=opcao_tema)
    ativo = models.BooleanField(default=True)
