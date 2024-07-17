# Generated by Django 5.0.6 on 2024-07-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0007_alter_book_options_alter_book_authors_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "default_related_name": "%(app_label)s_%(model_name)s",
                "ordering": ("-title",),
            },
        ),
        migrations.AlterModelOptions(
            name="bookauthor",
            options={"verbose_name_plural": "Books and Authors"},
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="bookauthor",
            name="role",
            field=models.CharField(
                choices=[
                    ("author", "Author"),
                    ("co_author", "Co-Author"),
                    ("editor", "Editor"),
                ],
                default="author",
                max_length=10,
            ),
        ),
    ]
