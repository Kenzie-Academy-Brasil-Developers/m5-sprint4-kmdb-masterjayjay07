# Generated by Django 4.0.5 on 2022-06-23 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='critic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='critic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='movie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_id', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='recomendation',
            field=models.CharField(choices=[('MW', 'Must Watch'), ('SW', 'Should Watch'), ('AW', 'Avoid Watch'), ('NO', 'No Opinion')], default='NO', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
