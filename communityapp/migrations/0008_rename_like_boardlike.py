# Generated by Django 4.0.5 on 2022-07-18 05:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communityapp', '0007_board_updated_at_alter_comment_board_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='BoardLike',
        ),
    ]
