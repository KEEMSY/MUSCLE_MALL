# Generated by Django 4.0.5 on 2022-07-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_remove_challenge_routine_challenge_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='kind',
            field=models.CharField(choices=[('food', 'Food'), ('exercise', 'Exercise')], max_length=20, verbose_name='종류'),
        ),
    ]