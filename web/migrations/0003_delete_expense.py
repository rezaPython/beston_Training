# Generated by Django 3.0.4 on 2020-03-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_income'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
    ]