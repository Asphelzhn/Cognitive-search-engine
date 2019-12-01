# Generated by Django 2.2.6 on 2019-10-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detecht_api', '0004_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword_distance',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('id_1', models.IntegerField()),
                ('id_2', models.IntegerField()),
                ('similarity', models.DecimalField(decimal_places=4,
                                                   max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
            ],
        ),
    ]
