# Generated by Django 4.0.5 on 2022-07-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0002_alter_board_user_alter_boardcategory_kind_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcategory',
            name='kind',
            field=models.CharField(choices=[('Free', 'Free'), ('Notice', 'Notice')], max_length=20, verbose_name='종류'),
        ),
    ]
