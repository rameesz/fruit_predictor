# Generated by Django 5.1.1 on 2024-10-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit1', models.CharField(max_length=50)),
                ('fruit2', models.CharField(max_length=50)),
                ('fruit3', models.CharField(max_length=50)),
                ('fruit4', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=100)),
            ],
        ),
    ]
