# Generated by Django 4.2.3 on 2023-07-13 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedme', '0006_user_feed_history_user_keywords_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reccomendations',
            new_name='recommendations',
        ),
    ]
