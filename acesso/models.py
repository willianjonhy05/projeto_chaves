from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
import qrcode
from django.db.models.signals import post_save
from io import BytesIO
import datetime

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField("Email")
    cpf = models.CharField(max_length=11, null=True, blank=True)
    usuario = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, related_name= 'funcionario')    
    funcao = models.CharField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome + " " + self.funcao
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['nome']


class Predio(models.Model):
    nome = models.CharField('Nome', max_length=100)
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    cep = models.CharField('CEP', max_length=9)  # O atributo para CEP
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')    

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Prédio"
        verbose_name_plural = "Prédios"
        ordering = ['nome']


class Sala(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    numero = models.CharField('Número da Sala', max_length=10)
    predio = models.ForeignKey(Predio, verbose_name='Prédio', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} - {}".format(self.predio, self.numero)
    
    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['numero']

    
class Chave(models.Model):
    disponivel = models.BooleanField('Disponivel',default=True)
    sala = models.ForeignKey(Sala, on_delete= models.CASCADE, related_name= 'chaves')
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.sala.numero, self.sala.descricao)
    
    class Meta:
        verbose_name = "Chave"
        verbose_name_plural = "Chaves"
        ordering = ['sala']

@receiver(post_save, sender=Chave)
def criar_qrcode(sender, instance, created, **kwargs):
    if created:
        sala_numero = instance.id
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code.add_data(sala_numero)
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image()

        stream = BytesIO()
        qr_code_image.save(stream, "PNG")
        instance.qr_code.save(f'{instance.sala.numero}.png', stream)
   

class Aluguel(models.Model):
    usuario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, related_name='usuario_alugueis')
    chave = models.ForeignKey(Chave, on_delete=models.DO_NOTHING, related_name='alugueis') 
    data_aluguel = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)