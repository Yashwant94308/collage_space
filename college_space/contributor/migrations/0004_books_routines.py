# Generated by Django 3.1.1 on 2020-09-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contributor', '0003_delete_routines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_description', models.CharField(blank=True, max_length=255)),
                ('books_document', models.FileField(upload_to='documents/')),
                ('books_uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_routine', models.CharField(blank=True, max_length=255)),
                ('document_routine', models.FileField(upload_to='documents/')),
                ('routine_uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]