# Generated by Django 3.1.4 on 2020-12-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_merge_20201226_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
