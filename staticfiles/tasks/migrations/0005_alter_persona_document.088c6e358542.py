# Generated by Django 4.0.6 on 2022-07-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_persona_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='document',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
