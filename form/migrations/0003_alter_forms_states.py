# Generated by Django 5.0.7 on 2024-07-27 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_remove_forms_states_forms_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='states',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.states'),
        ),
    ]
