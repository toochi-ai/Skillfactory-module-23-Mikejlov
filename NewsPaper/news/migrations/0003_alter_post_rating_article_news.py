# Generated by Django 5.1.2 on 2024-10-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_categorytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating_article_news',
            field=models.IntegerField(default=0),
        ),
    ]
