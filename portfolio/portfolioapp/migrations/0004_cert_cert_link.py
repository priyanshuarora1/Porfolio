# Generated by Django 3.0.4 on 2020-06-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_projects_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='cert',
            name='cert_link',
            field=models.CharField(default='#', max_length=500),
        ),
    ]