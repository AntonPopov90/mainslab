from django.db import models

class ExcelFile(models.Model):
    description = models.CharField(max_length=500, verbose_name='Описание', blank=True, null=True)
    excel_file = models.FileField(upload_to='media', null=True, blank=True)

class Client(models.Model):
    name = models.CharField(unique=True,max_length=100)
    number_of_organization = models.IntegerField(default=0)
    organization_sum = models.IntegerField(default=0)


