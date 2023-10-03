from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import  MinLengthValidator, RegexValidator
from decimal import Decimal

validate_any_character = RegexValidator(
    regex=r'^[\s\S]*$',
    message='Enter a valid text',
    code='invalid_text',
)

def validate_positive_decimal(value):
    if value <= Decimal('0'):
        raise ValidationError('O valor deve ser positivo.')

class Receipt(models.Model):
    name_recipient = models.CharField(max_length=100, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, validators=[validate_positive_decimal]) 
    referent = models.CharField(max_length=150, validators=[validate_any_character])
    name_sender = models.CharField(max_length=100, blank=False)
    sender_cpf = models.CharField(max_length=11, validators=[MinLengthValidator(limit_value=11)])
    date = models.DateField()

    def __str__(self):
        return self.name_recipient
