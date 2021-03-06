# Generated by Django 3.0.5 on 2020-04-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=130)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
