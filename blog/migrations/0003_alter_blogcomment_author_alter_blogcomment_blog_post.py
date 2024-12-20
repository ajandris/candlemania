# Generated by Django 5.1.4 on 2024-12-20 05:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogcomment_approved_alter_blogpost_slug_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(db_comment='Comment author', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='blog_post',
            field=models.ForeignKey(db_comment='Blog Post', on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blogpost'),
        ),
    ]
