# Generated by Django 4.0.1 on 2024-03-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abnormalactivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=500)),
            ],
        ),
    ]
