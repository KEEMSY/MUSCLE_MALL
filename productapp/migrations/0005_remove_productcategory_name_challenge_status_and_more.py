# Generated by Django 4.0.5 on 2022-06-29 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productapp', '0004_challenge_remove_routine_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='name',
        ),
        migrations.AddField(
            model_name='challenge',
            name='status',
            field=models.CharField(choices=[('시작 전', '시작 전'), ('진행 중', '진행 중'), ('완료', '완료')], default='시작 전', max_length=20),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='routine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.routine', verbose_name='루틴'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='kind',
            field=models.CharField(choices=[('exercise', 'Exercise'), ('food', 'Food')], max_length=20, verbose_name='종류'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.product', verbose_name='제품'),
        ),
        migrations.CreateModel(
            name='ProductDetailCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='세부 종류')),
                ('description', models.CharField(max_length=256, verbose_name='설명')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='productapp.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_category', to='productapp.productdetailcategory'),
        ),
    ]