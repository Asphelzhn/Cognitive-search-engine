# Generated by Django 2.2.5 on 2019-10-15 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detecht_api', '0005_keyword_distance_keywords'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='keyword_distance',
            unique_together={('id_1', 'id_2')},
        ),
    ]