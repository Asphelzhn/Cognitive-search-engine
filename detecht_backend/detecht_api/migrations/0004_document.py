# Generated by Django 2.2.5 on 2019-10-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detecht_api', '0003_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True,
                                          upload_to='detecht_api/static/pdf')),
            ],
        ),
    ]
