# Generated by Django 4.2.15 on 2024-08-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0004_alter_trainee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=100),
            preserve_default=False,
        ),
    ]
