# Generated by Django 4.2.5 on 2023-10-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_remove_anime_year_delete_animeyearstable_anime_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
