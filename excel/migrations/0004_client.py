# Generated by Django 4.0.4 on 2022-05-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0003_alter_excelfile_excel_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_organization', models.IntegerField(default=0)),
                ('organization_sum', models.IntegerField(default=0)),
            ],
        ),
    ]