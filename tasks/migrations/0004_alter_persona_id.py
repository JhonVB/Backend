# Generated by Django 4.0.6 on 2022-07-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_hobbie_persona_hobbie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
