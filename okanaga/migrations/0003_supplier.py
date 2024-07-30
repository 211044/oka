# Generated by Django 5.0.6 on 2024-07-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okanaga', '0002_alter_tabyouin_tabyouintel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('shiireid', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='仕入れ先 ID')),
                ('shiiremei', models.CharField(max_length=64, verbose_name='仕入れ先名')),
                ('shiireaddress', models.CharField(max_length=64, verbose_name='仕入れ先住所')),
                ('shiiretel', models.CharField(max_length=13, verbose_name='仕入れ先電話番号')),
                ('shihonkin', models.IntegerField(verbose_name='資本金')),
                ('nouki', models.IntegerField(help_text='発注して届く日数', verbose_name='納期')),
            ],
        ),
    ]