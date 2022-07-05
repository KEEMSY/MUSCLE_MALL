# Generated by Django 4.0.5 on 2022-07-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_user_bind_number_alter_coach_kind_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not Specified'), ('male', 'Male')], max_length=80, null=True, verbose_name='성별'),
        ),
    ]
