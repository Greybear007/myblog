# Generated by Django 3.1.2 on 2020-10-16 14:55

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
    ]