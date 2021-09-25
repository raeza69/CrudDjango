# Generated by Django 3.2.6 on 2021-09-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
