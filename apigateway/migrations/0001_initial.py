# Generated by Django 2.0 on 2018-11-08 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('request_path', models.CharField(max_length=255)),
                ('upstream_url', models.CharField(max_length=255)),
                ('plugin', models.IntegerField(choices=[(0, 'Remote auth'), (1, 'Basic auth'), (2, 'Key auth'), (3, 'Server auth')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apikey', models.CharField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='consumers',
            field=models.ManyToManyField(blank=True, to='apigateway.Consumer'),
        ),
    ]
