# Generated by Django 5.0.4 on 2024-05-01 02:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'age',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='age',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.age'),
        ),
    ]
