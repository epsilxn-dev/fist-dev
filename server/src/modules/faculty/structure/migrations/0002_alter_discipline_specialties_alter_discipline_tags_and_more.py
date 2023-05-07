# Generated by Django 4.0.2 on 2022-11-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='specialties',
            field=models.ManyToManyField(to='structure.Specialty', verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='tags',
            field=models.ManyToManyField(to='tags.Tags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='lessoner',
            name='disciplines',
            field=models.ManyToManyField(blank=True, to='structure.Discipline', verbose_name='Дисциплины'),
        ),
        migrations.AlterField(
            model_name='lessoner',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='stack_techs',
            field=models.ManyToManyField(to='structure.Techs'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='tags',
            field=models.ManyToManyField(to='tags.Tags', verbose_name='Теги'),
        ),
    ]
