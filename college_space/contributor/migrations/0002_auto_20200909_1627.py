# Generated by Django 3.1.1 on 2020-09-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.RemoveField(
            model_name='routines',
            name='document_routine',
        ),
    ]
