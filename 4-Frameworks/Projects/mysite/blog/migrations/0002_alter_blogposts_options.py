# Generated by Django 5.2.3 on 2025-06-27 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogposts",
            options={
                "ordering": ["created_at"],
                "verbose_name": "Blog Post",
                "verbose_name_plural": "Blog Posts",
            },
        ),
    ]
