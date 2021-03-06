# Generated by Django 3.1.2 on 2020-10-28 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('cover', models.ImageField(upload_to='covers', verbose_name='portada')),
            ],
        ),
    ]
