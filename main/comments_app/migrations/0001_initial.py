# Generated by Django 3.2.5 on 2021-07-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('content', models.TextField(verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email комментатора')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Комментарии')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_app', to='comments_app.articlemodel', verbose_name='Статья')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments_app.commentmodel', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
