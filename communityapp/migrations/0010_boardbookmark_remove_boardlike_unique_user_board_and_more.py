# Generated by Django 4.0.5 on 2022-07-18 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communityapp', '0009_boardlike_unique_user_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='boardlike',
            constraint=models.UniqueConstraint(fields=('user', 'board'), name='unique_user_board_like'),
        ),
        migrations.RemoveConstraint(
            model_name='boardlike',
            name='unique_user_board',
        ),
        migrations.AddField(
            model_name='boardbookmark',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_board', to='communityapp.board'),
        ),
        migrations.AddField(
            model_name='boardbookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='boardbookmark',
            constraint=models.UniqueConstraint(fields=('user', 'board'), name='unique_user_board_bookmark'),
        ),
    ]
