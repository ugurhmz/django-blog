# Generated by Django 3.1.7 on 2021-03-03 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_iletisimmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='yorum_duzenlenme_tarihi',
            new_name='duzenleme_tarihi',
        ),
        migrations.RenameField(
            model_name='yorummodel',
            old_name='yorum_olusturulma_tarihi',
            new_name='olusturulma_tarihi',
        ),
    ]