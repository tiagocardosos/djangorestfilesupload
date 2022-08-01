# Generated by Django 4.0.6 on 2022-07-31 19:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('simplefile', '0006_remove_simplefiledetails_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplefiledetails',
            name='full_path',
            field=models.CharField(blank=True, max_length=255, verbose_name='Full Path'),
        ),
        migrations.AlterField(
            model_name='simplefiledetails',
            name='identifier',
            field=models.UUIDField(default=uuid.UUID('456e9a44-855a-4e8b-ae10-64d02be396a2'), verbose_name='Identifier'),
        ),
    ]
