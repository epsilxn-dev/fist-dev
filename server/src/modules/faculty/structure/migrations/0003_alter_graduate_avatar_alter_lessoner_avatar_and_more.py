# Generated by Django 4.0.3 on 2022-11-27 08:55

from django.db import migrations, models
import src.modules.faculty.structure.models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_alter_discipline_specialties_alter_discipline_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='avatar',
            field=models.ImageField(default='not-found.png', upload_to=src.modules.faculty.structure.models.get_path_for_graduate_image, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='lessoner',
            name='avatar',
            field=models.ImageField(default='not-found.png', upload_to=src.modules.faculty.structure.models.get_path_for_lessoner_image, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='avatar',
            field=models.ImageField(default='not-found.png', upload_to='specialty_image', verbose_name='Изображение направления'),
        ),
    ]