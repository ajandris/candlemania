# Generated by Django 5.1.4 on 2024-12-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='approved',
            field=models.BooleanField(db_comment='Comment Approval status', default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(db_comment='Blog post slug', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(db_comment='Blog title', max_length=250),
        ),
    ]
