# Generated by Django 4.1.13 on 2024-06-28 15:03

import books.models.book
import bson.objectid
from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True,
                        default=bson.objectid.ObjectId,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
            ],
            options={
                "verbose_name": "author",
                "verbose_name_plural": "author",
                "db_table": "books_author",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True,
                        default=bson.objectid.ObjectId,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "publication_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "author",
                    djongo.models.fields.EmbeddedField(
                        model_container=books.models.book.EmbeddedAuthor
                    ),
                ),
            ],
            options={
                "verbose_name": "book",
                "verbose_name_plural": "book",
                "db_table": "books_book",
            },
        ),
    ]