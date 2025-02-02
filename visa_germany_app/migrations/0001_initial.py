# Generated by Django 3.1.2 on 2021-03-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=800)),
                ('url', models.URLField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
