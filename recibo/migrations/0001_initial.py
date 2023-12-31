# Generated by Django 4.2.5 on 2023-10-03 13:28

import django.core.validators
from django.db import migrations, models
import re
import recibo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_recipient', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[recibo.models.validate_positive_decimal])),
                ('referent', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('name_sender', models.CharField(max_length=100)),
                ('sender_cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(limit_value=11)])),
                ('date', models.DateField()),
            ],
        ),
    ]
