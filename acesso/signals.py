from .models import Funcionario
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Chave
import qrcode
from io import BytesIO
from django.core.files import File



@receiver(post_save, sender=get_user_model())
def create_usuario(sender, instance, created, **kwargs):
    if created:
        funcionario = Funcionario.objects.create(nome=instance.get_full_name(), email=instance.email, user=instance)


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
        stream.seek(0)
        instance.qr_code.save(f'{instance.sala.numero}.png', File(stream))