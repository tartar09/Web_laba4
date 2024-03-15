# Generated by Django 4.2.1 on 2024-03-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipes',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AddIndex(
            model_name='recipes',
            index=models.Index(fields=['-time_create'], name='recipes_rec_time_cr_d08964_idx'),
        ),
    ]