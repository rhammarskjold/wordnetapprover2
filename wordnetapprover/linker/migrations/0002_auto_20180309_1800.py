# Generated by Django 2.0.3 on 2018-03-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposedlink',
            name='link_weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset1def',
            field=models.CharField(default='no definition', max_length=200),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset1pos',
            field=models.CharField(default='n', max_length=1),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset1words',
            field=models.CharField(default='no_words', max_length=200),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset2def',
            field=models.CharField(default='no definition', max_length=200),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset2pos',
            field=models.CharField(default='n', max_length=1),
        ),
        migrations.AddField(
            model_name='proposedlink',
            name='synset2words',
            field=models.CharField(default='no_words', max_length=200),
        ),
        migrations.AlterField(
            model_name='proposedlink',
            name='assigned_user',
            field=models.CharField(default='no user', max_length=80),
        ),
    ]