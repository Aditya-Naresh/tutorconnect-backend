# Generated by Django 5.0.6 on 2024-06-25 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='tutor',
            new_name='owner',
        ),
    ]
