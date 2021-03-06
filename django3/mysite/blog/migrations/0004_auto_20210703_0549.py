# Generated by Django 3.2.5 on 2021-07-03 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_school_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('1', 'Средняя'), ('2', 'Гимназия'), ('3', 'Лицей'), ('4', 'Частная'), ('5', 'Интернат'), ('6', 'Спорт Школа')], default='Школа', max_length=255),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('experiance', models.IntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='blog.school')),
            ],
        ),
    ]
