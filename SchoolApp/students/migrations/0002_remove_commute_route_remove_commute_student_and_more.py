# Generated by Django 5.0.3 on 2024-03-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commute',
            name='route',
        ),
        migrations.RemoveField(
            model_name='commute',
            name='student',
        ),
        migrations.RemoveField(
            model_name='commute',
            name='transportation',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='distance_to_school',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Commute',
        ),
        migrations.DeleteModel(
            name='Transportation',
        ),
    ]