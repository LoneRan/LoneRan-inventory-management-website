# Generated by Django 3.0.8 on 2020-12-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=20)),
                ('temp', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
                ('co2', models.CharField(max_length=20)),
                ('o2', models.CharField(max_length=20)),
                ('freshlevel', models.CharField(max_length=20)),
            ],
        ),
    ]
