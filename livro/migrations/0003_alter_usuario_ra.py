# Generated by Django 4.0.5 on 2022-06-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_alter_emprestimo_ra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ra',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
