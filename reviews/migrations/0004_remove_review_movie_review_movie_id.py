# Generated by Django 4.0.5 on 2022-06-23 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('reviews', '0003_remove_review_movie_id_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_id', to='movies.movie'),
        ),
    ]
