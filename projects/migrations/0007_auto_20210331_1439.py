# Generated by Django 2.2.12 on 2021-03-31 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210331_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Category'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='projects',
            field=models.ManyToManyField(to='projects.Project'),
        ),
    ]
