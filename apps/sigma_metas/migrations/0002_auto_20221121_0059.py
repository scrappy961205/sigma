# Generated by Django 3.2.12 on 2022-11-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigma_metas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='tareas_id',
        ),
        migrations.AddField(
            model_name='plan',
            name='tareas_id',
            field=models.ManyToManyField(to='sigma_metas.Tarea', verbose_name='Tareas'),
        ),
    ]
