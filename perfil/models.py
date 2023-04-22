from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.validador_cpf import validar_cpf
import re


class Perfil(models.Model):
    Usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuário")
    idade = models.PositiveBigIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)

    endereco = models.CharField(max_length=50)
    numero_endereco = models.CharField(max_length=5)
    complemento_endereco = models.CharField(max_length=30)
    bairro_endereco = models.CharField(max_length=30)
    cep_endereco = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default="SP",
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self) -> str:
        return f"{self.Usuario}"

    def clean(self) -> None:
        error_massages = {}
        if not validar_cpf(self.cpf):
            error_massages["cpf"] = "Digite um CPF válido"

        if re.search(r"[^0-9]", self.cep_endereco) or len(self.cep_endereco) < 8:
            error_massages["cep_endereco"] = "Digite um CEP válido"

        if error_massages:
            raise ValidationError(error_massages)

    class Meta:
        verbose_name = "Pefil"
        verbose_name_plural = "Perfis"
