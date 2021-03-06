# Generated by Django 3.1.5 on 2021-01-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('prompt', models.CharField(max_length=200)),
                ('correctAnswer', models.BooleanField(default=None)),
                ('userAnswer', models.BooleanField(default=None)),
            ],
        ),
    ]
