# Generated by Django 3.0.2 on 2020-02-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_auto_20200216_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]