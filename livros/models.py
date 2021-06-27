from django.db import models

class Livro(models.Model):
    STATUS_CHOICE = (('Finalizado', 'Finalizado'), ('Lendo','Lendo'))
    livro = models.CharField(max_length=200)
    finalizado = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Lendo')
    resumo = models.TextField()
    adicionado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.livro
    
    class Meta:
        ordering = ['adicionado']