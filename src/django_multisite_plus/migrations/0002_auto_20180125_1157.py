# Generated by Django 1.10.8 on 2018-01-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_multisite_plus", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="site",
            name="extra_uwsgi_ini",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="site",
            name="is_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Whether this site should be served and available.",
            ),
        ),
        migrations.AddField(
            model_name="site",
            name="last_updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
