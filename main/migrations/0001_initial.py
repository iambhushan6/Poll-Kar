# Generated by Django 3.2.4 on 2021-06-13 05:36

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
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('option_one', models.CharField(max_length=56)),
                ('option_two', models.CharField(max_length=56)),
                ('option_three', models.CharField(max_length=56)),
                ('option_four', models.CharField(max_length=56)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('option_four_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
