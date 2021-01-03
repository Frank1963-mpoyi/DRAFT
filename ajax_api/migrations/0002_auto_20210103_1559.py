# Generated by Django 3.0.8 on 2021-01-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='BRAND'),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='picture',
            field=models.ImageField(upload_to='shirts', verbose_name='PICTURE'),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRICE'),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='visited',
            field=models.IntegerField(verbose_name='VISITED'),
        ),
    ]