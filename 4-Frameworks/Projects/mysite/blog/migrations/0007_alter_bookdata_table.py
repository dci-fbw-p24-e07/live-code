# Generated by Django 5.2.3 on 2025-07-02 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_book_pages_gte_50_book_price_lte_100"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="bookdata",
            table="book_data",
        ),
    ]
