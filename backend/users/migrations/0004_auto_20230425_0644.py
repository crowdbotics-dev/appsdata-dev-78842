# Generated by Django 2.2.28 on 2023-04-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230425_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='jhsddfdsh',
        ),
        migrations.AddField(
            model_name='user',
            name='dgzdfg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hjgshjsd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]