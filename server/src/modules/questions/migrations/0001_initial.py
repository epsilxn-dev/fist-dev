# Generated by Django 4.0.3 on 2022-11-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта автора')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('is_ready_to_publish', models.BooleanField(default=False, verbose_name='Готово к публикации?')),
                ('theme', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Тема')),
                ('tags', models.ManyToManyField(to='tags.tags', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'fc_questions',
                'ordering': ['id'],
            },
        ),
    ]
