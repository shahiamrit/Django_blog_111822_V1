# Generated by Django 4.1.3 on 2022-11-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_001', '0002_category_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
    ]
