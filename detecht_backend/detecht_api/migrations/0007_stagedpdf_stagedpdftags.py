# Generated by Django 2.2.5 on 2019-11-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detecht_api', '0006_auto_20191015_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='stagedPdf',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('pdf_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stagedPdfTags',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('staged_pdf_id', models.IntegerField()),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
    ]
