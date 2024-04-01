# Generated by Django 4.2.11 on 2024-04-01 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_subasta_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='subasta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.subasta'),
            preserve_default=False,
        ),
    ]