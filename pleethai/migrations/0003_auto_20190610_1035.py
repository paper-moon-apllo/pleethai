# Generated by Django 2.1.2 on 2019-06-10 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pleethai', '0002_auto_20190609_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysWordJapanese',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('japanese', models.CharField(max_length=127)),
                ('hiragana', models.CharField(max_length=127)),
                ('roman', models.CharField(blank=True, max_length=127, null=True)),
                ('searchs', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wordclass_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pleethai.WordClass')),
            ],
        ),
        migrations.CreateModel(
            name='SysWordThai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thai', models.CharField(max_length=127)),
                ('pronunciation_symbol', models.CharField(blank=True, max_length=127, null=True)),
                ('pronunciation_kana', models.CharField(blank=True, max_length=127, null=True)),
                ('english', models.CharField(blank=True, max_length=127, null=True)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('japanese_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pleethai.SysWordJapanese')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together={('japanese', 'hiragana', 'thai')},
        ),
        migrations.AlterUniqueTogether(
            name='syswordthai',
            unique_together={('japanese_id', 'thai')},
        ),
        migrations.AlterUniqueTogether(
            name='syswordjapanese',
            unique_together={('japanese', 'hiragana')},
        ),
    ]
