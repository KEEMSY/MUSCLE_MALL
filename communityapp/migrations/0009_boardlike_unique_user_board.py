# Generated by Django 4.0.5 on 2022-07-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0008_rename_like_boardlike'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='boardlike',
            constraint=models.UniqueConstraint(fields=('user', 'board'), name='unique_user_board'),
        ),
    ]
