# Generated by Django 4.0.3 on 2022-11-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratories', '0003_alter_laboratory_areas_alter_laboratory_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='image',
            field=models.ImageField(default='not-found.png', upload_to='laboratories'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='not-found.png', upload_to='projects'),
        ),
    ]
