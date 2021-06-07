from django.db import models


# Create your models here.
class Routines(models.Model):
    routine_description = models.CharField(max_length=255)
    routine_uploader_name = models.CharField(max_length=205)
    document_routine = models.FileField(upload_to='documents/')
    routine_uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.routine_description


class Books(models.Model):
    books_description = models.CharField(max_length=225)
    books_uploader_name = models.CharField(max_length=205)
    books_document = models.FileField(upload_to='documents/')
    books_uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.books_description


