# Generated by Django 5.0.6 on 2024-05-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='filmes/'),
        ),
    ]
