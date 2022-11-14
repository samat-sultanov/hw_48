# Generated by Django 4.1.3 on 2022-11-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание товара')),
                ('category', models.CharField(choices=[('other', 'разное'), ('food', 'еда'), ('drinks', 'напитки')], default='other', max_length=30)),
                ('balance', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
            ],
        ),
    ]