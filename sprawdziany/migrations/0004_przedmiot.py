# Generated by Django 2.2 on 2019-05-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprawdziany', '0003_sprawdzian_klasa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]