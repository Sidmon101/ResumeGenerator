# Generated by Django 5.1.6 on 2025-06-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='template_choice',
            field=models.CharField(choices=[('template1', 'Classic'), ('template2', 'Modern'), ('template3', 'Elegant')], default='template1', max_length=20),
        ),
    ]
