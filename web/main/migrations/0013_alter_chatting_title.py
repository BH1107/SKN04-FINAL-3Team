# Generated by Django 5.1.2 on 2025-01-10 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_chatting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatting',
            name='title',
            field=models.CharField(default='', max_length=10),
        ),
    ]
